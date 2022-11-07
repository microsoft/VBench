# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
import argparse
import csv
import torch
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('--path-numbers', type=str, default="./vbench/collections/numbers.tsv",
                    help='path to number data')
parser.add_argument('--path-text', type=str, default="./vbench/collections/text.tsv",
                    help='path to text data')
parser.add_argument('--path-or-filter', type=str, default="./vbench/queries/or_filter.tsv",
                    help='path to queries filter')
parser.add_argument('--path-and-filter', type=str, default="./vbench/queries/and_filter.tsv",
                    help='path to queries filter')
parser.add_argument('--path-img-embeddings', type=str, default="./vbench/collections/img_embeds_collection.tsv",
                    help='path to img embeddings')
parser.add_argument('--path-img-queries', type=str, default="./vbench/queries/img_embeds_query.tsv",
                    help='path to img queries')
args = parser.parse_args()

SIZE_COLLECTION = 330922

def plot_selectivity_distribution(counts, title, path):
    selectivities = [cnt / SIZE_COLLECTION for cnt in counts]
    plt.hist(selectivities, 50)
    plt.title(title)
    plt.savefig(path)
    plt.close()

def get_or_selectivity():
    number_ingredients = []
    number_instructions = []

    with open(args.path_numbers, 'r', encoding="utf8") as f:
        tsvreader = csv.reader(f, delimiter="\t")
        idx = 0
        for _, count, step in tsvreader:
            idx += 1
            number_ingredients.append(int(count))
            number_instructions.append(int(step))
    print("Finish loading numbers.")
    with open(args.path_or_filter, 'r', encoding="utf8") as f_or_filter:
        or_filters = csv.reader(f_or_filter, delimiter="\t")
        counts = []
        for idx, filter1, filter2 in or_filters:
            cnt = 0
            for number_ingredient, number_instruction in zip(number_ingredients, number_instructions):
                if number_ingredient < int(filter1) or number_instruction < int(filter2):
                    cnt += 1
            counts.append(cnt)
        print(f"Selectivity of `or` filter: {(sum(counts) / len(counts)) / SIZE_COLLECTION}")

        plot_selectivity_distribution(counts, "Selectivity Distribution of the Or Filter", "./filter_generation/img/selectivity-distribution-or.png")

def get_and_selectivity():
    texts = []
    with open(args.path_text, 'r', encoding="utf8") as f:
        tsvreader = csv.reader(f, delimiter="\t")
        idx = 0
        for _, ingredients, instructions in tsvreader:
            idx += 1
            texts.append(ingredients + instructions)
    print("Finish loading text.")
    with open(args.path_and_filter, 'r', encoding="utf8") as f_filter:
        filters = csv.reader(f_filter, delimiter="\t")
        counts = []
        for idx, (_, filter1, filter2) in enumerate(filters):
            cnt = 0
            for text in texts:
                if filter1.replace('_', ' ') in text and filter2.replace('_', ' ') not in text:
                    cnt += 1
            counts.append(cnt)
            if idx % 50 == 0:
                print(f"{idx} queries searched...")
        print(f"Selectivity of `and` filter: {(sum(counts) / len(counts)) / SIZE_COLLECTION}")

        plot_selectivity_distribution(counts, "Selectivity Distribution of the And Filter", "./filter_generation/img/selectivity-distribution-and.png")

def get_ranger_selectivity():
    im_vecs = []
    with open(args.path_img_embeddings, 'r', encoding="utf8") as f:
        tsvreader = csv.reader(f, delimiter="\t")
        for _, vec in tsvreader:
            vec = [float(ele) for ele in vec[1:-1].split(', ')]
            im_vecs.append(vec)
    print("Finish loading image collection.")

    device = torch.device('cuda:0')
    im_vecs = torch.Tensor(im_vecs).to(device)  # [N, D]

    with open(args.path_img_queries, 'r', encoding="utf8") as f_query_image:
        query_image = csv.reader(f_query_image, delimiter="\t")
        counts = []
        for _, img_vec in query_image:
            img_vec = [float(ele) for ele in img_vec[1:-1].split(', ')]
            img_vec = torch.Tensor(img_vec).to(device)  # [D]
            cosinesimilarity = torch.mm(img_vec.unsqueeze(0), im_vecs.transpose(0, 1))
            counts.append(torch.sum(cosinesimilarity > 0.9).detach().cpu())
        print(f"Selectivity of `Range R` filter: {(sum(counts) / len(counts)) / im_vecs.shape[0]}")

        plot_selectivity_distribution(counts, "Selectivity Distribution of the RangeR Filter", "./filter_generation/img/selectivity-distribution-ranger.png")

if __name__ == "__main__":
    get_or_selectivity()
    get_and_selectivity()
    get_ranger_selectivity()
