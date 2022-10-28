# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
import random
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--path-numbers', type=str, default="../vbench/collections/numbers.tsv",
                    help='path to number data')
parser.add_argument('--path-queries-ingredients', type=str, default="../vbench/queries/keywords.tsv",
                    help='path to queries ingredients')
parser.add_argument('--path-result', type=str, default="../vbench/queries/numeric_filter.tsv",
                    help='path to save result')
args = parser.parse_args()

number_instructions = []
with open(args.path_numbers, 'r', encoding="utf8") as f:
    tsvreader = csv.reader(f, delimiter="\t")
    idx = 0
    for _, count, step in tsvreader:
        idx += 1
        number_instructions.append(int(step))

number_instructions = sorted(number_instructions)
SIZE_COLLECTION = len(number_instructions)
SIZE_QUERY = 10000
# random.seed(0)
# filters = random.sample(number_instructions, SIZE_QUERY)

queries = csv.reader(open(args.path_queries_ingredients, 'r', encoding="utf8"), delimiter="\t")
with open(args.path_result, 'w', encoding="utf8") as out:
    for idx, query in enumerate(queries):
        qid = query[0]
        out.write(f"{qid}\t{number_instructions[int(SIZE_COLLECTION / SIZE_QUERY * idx)]}\n")
        # out.write(f"{qid}\t{filters[idx]}\n")
