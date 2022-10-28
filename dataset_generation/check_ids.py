# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument('--path-img-embeddings',type=str, default="./vbench/collections/img_embeds.tsv",
                    help='path to img embeddings')
parser.add_argument('--path-text-embeddings',type=str, default="./vbench/collections/rec_embeds.tsv",
                    help='path to text embeddings')
parser.add_argument('--path-numbers',type=str, default="./vbench/numbers.tsv",
                    help='path to numbers')
parser.add_argument('--path-text-data',type=str, default="./vbench/text.tsv",
                    help='path to text data')
parser.add_argument('--path-img-queries', type=str, default="./vbench/queries/img_embeds.tsv",
                    help='path to img queries')
parser.add_argument('--path-text-queries', type=str, default="./vbench/queries/rec_embeds.tsv",
                    help='path to text queries')
parser.add_argument('--path-query-filter', type=str, default="./vbench/queries/or_filter.tsv",
                    help='path to queries filter')
parser.add_argument('--path-query-and-filter', type=str, default="./vbench/queries/and_filter.tsv",
                    help='path to queries and filter')
parser.add_argument('--path-query-text', type=str, default="./vbench/queries/text.tsv",
                    help='path to queries text')
args = parser.parse_args()

qids = []
qids_1 = []
qids_2 = []
qids_3 = []
qids_4 = []
with open(args.path_img_queries, 'r', encoding="utf8") as f:
    tsvreader = csv.reader(f, delimiter="\t")
    for qid, vec in tsvreader:
        qids.append(qid)
print("Finish loading image queries.")

with open(args.path_text_queries, 'r', encoding="utf8") as f:
    tsvreader = csv.reader(f, delimiter="\t")
    for qid, vec in tsvreader:
        qids_1.append(qid)
assert qids == qids_1
print("Finish loading text queries.")

with open(args.path_query_filter, 'r', encoding="utf8") as f:
    tsvreader = csv.reader(f, delimiter="\t")
    for qid, count, step in tsvreader:
        qids_2.append(qid)
assert qids_1 == qids_2
print("Finish loading filter queries.")

with open(args.path_query_and_filter, 'r', encoding="utf8") as f:
    tsvreader = csv.reader(f, delimiter="\t")
    for qid, _, _ in tsvreader:
        qids_3.append(qid)
assert qids_1 == qids_3
print("Finish loading and filter queries.")

with open(args.path_query_text, 'r', encoding="utf8") as f:
    tsvreader = csv.reader(f, delimiter="\t")
    for qid, _, _ in tsvreader:
        qids_4.append(qid)
assert qids_1 == qids_4
print("Finish loading text queries.")

rids = []
rids_1 = []
rids_2 = []
rids_3 = []


with open(args.path_img_embeddings, 'r', encoding="utf8") as f:
    tsvreader = csv.reader(f, delimiter="\t")
    for rid, vec in tsvreader:
        rids.append(rid)
print("Finish loading image collection.")

with open(args.path_text_embeddings, 'r', encoding="utf8") as f:
    tsvreader = csv.reader(f, delimiter="\t")
    for rid, vec in tsvreader:
        rids_1.append(rid)
assert rids == rids_1
print("Finish loading text collection.")

with open(args.path_numbers, 'r', encoding="utf8") as f:
    tsvreader = csv.reader(f, delimiter="\t")
    for rid, count, step in tsvreader:
        rids_2.append(rid)
for idx, (rid1, rid2) in enumerate(zip(rids_1, rids_2)):
    if rid1 != rid2:
        print(idx, rid1, rid2)
assert rids_1 == rids_2

print("Finish loading additional collection.")

with open(args.path_text_data, 'r', encoding="utf8") as f:
    tsvreader = csv.reader(f, delimiter="\t")
    for rid, _, _ in tsvreader:
        rids_3.append(rid)
for idx, (rid1, rid3) in enumerate(zip(rids_1, rids_3)):
    if rid1 != rid3:
        print(idx, rid1, rid3)
assert rids_1 == rids_3

print("Finish loading text collection.")
