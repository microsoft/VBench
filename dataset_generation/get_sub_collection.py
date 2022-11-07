# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
import argparse
import os
import pickle
import random

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--path-collection', type=str, default="vbench/collections",
                        help='collection')
    parser.add_argument('--size-subcollection', type=int, default=10000,
                        help='size of subcollection')
    parser.add_argument('--path-result', type=str, default="vbench/collections/10k",
                        help='result')
    args = parser.parse_args()

    SIZE_COLLECTION = 330922
    SIZE_SUBCOLLECTION = args.size_subcollection

    random.seed(0)
    lines_subcollection = random.sample(list(range(SIZE_COLLECTION)), SIZE_SUBCOLLECTION)

    files = ['img_embeds_collection.tsv', 'rec_embeds_collection.tsv', 'numbers.tsv', 'text.tsv']

    for f in files:
        with open(os.path.join(args.path_collection, f), 'r', encoding="utf8") as in_f, \
            open(os.path.join(args.path_result, f), 'w', encoding="utf8") as out_f:
            idx = 0
            while idx < SIZE_COLLECTION:
                l= in_f.readline()

                if idx in lines_subcollection:
                    out_f.write(l)
                idx += 1

    print("Finished!")
