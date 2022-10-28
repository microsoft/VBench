# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--partition', dest='partition', default='query')
parser.add_argument('--path-result', type=str, default="../vbench/queries/price.tsv",
                    help='path to save result')
args = parser.parse_args()

SIZE_QUERY = 10000
SIZE_COLLECTION = 330922
random.seed(0)
ids = list(range(SIZE_QUERY + SIZE_COLLECTION))
qids = sorted(random.sample(ids, SIZE_QUERY))
cids = [tid for tid in ids if tid not in qids]

if args.partition == 'query':
    with open(args.path_result, 'w', encoding="utf8") as out:
        for idx, qid in enumerate(qids):
            out.write(f"{qid}\t{idx+1}\n")
else:
    with open(args.path_result, 'w', encoding="utf8") as out:
        for idx, cid in enumerate(cids):
            out.write(f"{cid}\t{random.randint(1, 10000)}\n")
