# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
import argparse
import os
import csv
import torch

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--filter', type=str, default='no',
                        help='no, number, string')
    parser.add_argument('--k', type=int, default=50,
                        help='top k')
    parser.add_argument('--path-img-embeddings', type=str, default="./data/vbench/collections/img_embeds.tsv",
                        help='path to img embeddings')
    parser.add_argument('--path-number-data', type=str, default="./data/vbench/collections/numbers.tsv",
                        help='path to number data')
    parser.add_argument('--path-text-data', type=str, default="./data/vbench/collections/text.tsv",
                        help='path to text data')
    parser.add_argument('--path-img-queries', type=str, default="./data/vbench/queries/img_embeds.tsv",
                        help='path to img queries')
    parser.add_argument('--path-query-filter', type=str, default="./data/vbench/queries/price.tsv",
                        help='path to queries filter')
    parser.add_argument('--path-results', type=str, default="./qrels-exact-top50.tsv",
                        help='path to save exact result')
    parser.add_argument('--log-frequency', type=int, default=100,
                        help='log frequency')
    parser.add_argument('--start-line', type=int, default=0,
                        help='start line')
    parser.add_argument('--end-line', type=int, default=0,
                        help='end line')
    args = parser.parse_args()

    rids = []
    im_vecs = []
    number_ingredients = []
    number_instructions = []
    ingre = []
    instru = []
    with open(args.path_img_embeddings, 'r', encoding="utf8") as f:
        tsvreader = csv.reader(f, delimiter="\t")
        idx = 0
        for rid, vec in tsvreader:
            idx += 1
            vec = [float(ele) for ele in vec[1:-1].split(', ')]
            im_vecs.append(vec)
            rids.append(rid)
    print("Finish loading image collection.")

    with open(args.path_number_data, 'r', encoding="utf8") as f:
        tsvreader = csv.reader(f, delimiter="\t")
        idx = 0
        for rid, count, step in tsvreader:
            idx += 1
            number_ingredients.append(int(count))
            number_instructions.append(int(step))
    print("Finish loading number collection.")

    device = torch.device('cuda:0')
    im_vecs = torch.Tensor(im_vecs).to(device)  # [N, D]
    number_ingredients = torch.Tensor(number_ingredients).to(device).unsqueeze(0)  # [1,N]
    number_instructions = torch.Tensor(number_instructions).to(device).unsqueeze(0)  # [1,N]

    with open(args.path_img_queries, 'r', encoding="utf8") as f_query_image, \
            open(args.path_query_filter, 'r', encoding="utf8") as f_query_filter, \
            open(os.path.join(args.path_results), 'w', encoding="utf8") as out:
        query_image = csv.reader(f_query_image, delimiter="\t")
        query_filter = csv.reader(f_query_filter, delimiter="\t")
        for idx, ((qid, img_vec), (_, filter1)) in enumerate(zip(query_image, query_filter)):
            if idx < args.start_line:
                continue
            if idx > args.end_line:
                break
            img_vec = [float(ele) for ele in img_vec[1:-1].split(', ')]
            img_vec = torch.Tensor(img_vec).to(device)  # [D]
            cosinesimilarity = torch.mm(img_vec.unsqueeze(0), im_vecs.transpose(0, 1))
            if args.filter == 'number':
                price = int(filter1)
                cosinesimilarity[number_ingredients > price] = -2
            elif args.filter == 'string':
                ingre_bool = []
                with open(args.path_text_data, 'r', encoding="utf8") as f:
                    tsvreader = csv.reader(f, delimiter="\t")
                    for _, ingredients, instructions in tsvreader:
                        text = ingredients + instructions
                        if filter1.replace('_', ' ') not in text:
                            ingre_bool.append(True)
                        else:
                            ingre_bool.append(False)
                ingre_bool = torch.Tensor(ingre_bool).to(device).unsqueeze(0).to(torch.bool)
                cosinesimilarity[ingre_bool] = -2
            scores, indices = torch.topk(
                cosinesimilarity, args.k, dim=1)  # [1, K]

            scores = scores.squeeze().detach().tolist()
            indices = indices.squeeze().detach().tolist()
            for i, index in enumerate(indices):
                rid = rids[index]
                rank = i+1
                out.write(f"{qid}\t{rid}\t{rank}\t{scores[i]}\n")

            if (idx+1) % args.log_frequency == 0:
                out.flush()
                print(f"{idx+1} queries searched...")

    print("search finished.")
