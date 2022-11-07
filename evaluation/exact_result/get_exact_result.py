# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
import argparse
import os
import pickle
import random
from scipy import spatial
import numpy as np

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--path-embeddings', nargs='+',
                        help='path to embeddings')
    parser.add_argument('--k', type=int, default=50,
                        help='top k')
    parser.add_argument('--path-results', type=str, default="../result/Recipe1M/qrels-exact-top50.tsv",
                        help='path to save exact result')
    parser.add_argument('--log-frequency', type=int, default=100,
                        help='log frequency')
    parser.add_argument('--queries', type=int, default=0,
                        help='number of queries')
    parser.add_argument('--start-line', type=int, default=0,
                        help='start line')

    args = parser.parse_args()

    im_vecs = []
    instr_vecs = []
    for path in args.path_embeddings:
        with open(os.path.join(path, 'img_embeds.pkl'), 'rb') as f:
            im_vecs += pickle.load(f).tolist()
        with open(os.path.join(path, 'rec_embeds.pkl'), 'rb') as f:
            instr_vecs += pickle.load(f).tolist()

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
    qids.sort()
    rids = list(set(ids) - set(qids))

    im_vecs_query = [im_vecs[i] for i in qids]
    im_vecs_collection = [im_vecs[i] for i in rids]
    instr_vecs_query = [instr_vecs[i] for i in qids]
    instr_vecs_collection = [instr_vecs[i] for i in rids]

    with open(os.path.join(args.path_results), 'w', encoding="utf8") as out:
        for idx, (im_vec_query, instr_vec_query) in enumerate(zip(im_vecs_query, instr_vecs_query)):
            if idx < args.start_line:
                continue
            distances = list(map(
                lambda im_vec, instr_vec: spatial.distance.cosine(
                    im_vec, im_vec_query) + spatial.distance.cosine(instr_vec, instr_vec_query),
                im_vecs_collection,
                instr_vecs_collection
            ))  # distance = 2 - score

            qid = qids[idx]
            indexes = np.argsort(distances)  # ascending
            for i, index in enumerate(indexes[:args.k]):
                rid = rids[index]
                rank = i+1
                out.write(f"{qid}\t{rid}\t{rank}\n")

            if (idx+1) % args.log_frequency == 0:
                out.flush()
                print(f"{idx+1} queries searched...")
        print("search finished.")
