# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
import argparse
import os
import pickle
import random

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--path-embeddings', nargs='+',
                        help='path to embeddings')
    parser.add_argument('--path-results', type=str, default="vbench/",
                        help='path to save split result')
    parser.add_argument('--queries', type=int, default=0,
                        help='number of queries')
    args = parser.parse_args()

    im_vecs = []
    instr_vecs = []
    for path in args.path_embeddings:
        with open(os.path.join(path, 'img_embeds.pkl'), 'rb') as f:
            im_vecs += pickle.load(f).tolist()
        with open(os.path.join(path, 'rec_embeds.pkl'), 'rb') as f:
            instr_vecs += pickle.load(f).tolist()
    print(f"Number of image vectors: {len(im_vecs)}")
    print(f"Number of instr vectors: {len(instr_vecs)}")

    if not args.queries:
        SIZE_QUERY = int(len(im_vecs) * 0.1)  # use 10% as query by default
    else:
        SIZE_QUERY = args.queries
    print(f"Number of queries: {SIZE_QUERY}")
    SIZE_COLLECTION = len(im_vecs) - SIZE_QUERY
    print(f"Size of collections: {SIZE_COLLECTION}")
    random.seed(0)
    ids = list(range(len(im_vecs)))
    qids = random.sample(ids, SIZE_QUERY)

    print("Splitting...")
    idx = 0
    with open(os.path.join(args.path_results, 'queries/img_embeds.tsv'), 'w', encoding="utf8") as out_img_embeds_query, \
            open(os.path.join(args.path_results, 'collections/img_embeds.tsv'), 'w', encoding="utf8") as out_img_embeds_collection, \
            open(os.path.join(args.path_results, 'queries/rec_embeds.tsv'), 'w', encoding="utf8") as out_rec_embeds_query, \
            open(os.path.join(args.path_results, 'collections/rec_embeds.tsv'), 'w', encoding="utf8") as out_rec_embeds_collection:

        for im_vec, instr_vec in zip(im_vecs, instr_vecs):
            if idx in qids:
                out_img_embeds_query.write(f"{idx}\t{im_vec}\n")
                out_rec_embeds_query.write(f"{idx}\t{instr_vec}\n")
            else:
                out_img_embeds_collection.write(f"{idx}\t{im_vec}\n")
                out_rec_embeds_collection.write(f"{idx}\t{instr_vec}\n")
            idx += 1

    print("Split finished!")
