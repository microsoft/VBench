# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
import random
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--path-queries-ingredients', type=str, default="../data/queries/ingredients_keywords.tsv",
                    help='path to queries ingredients')
parser.add_argument('--path-result', type=str, default="../data/queries/or_filter.tsv",
                    help='path to save result')
args = parser.parse_args()


random.seed(0)
queries = csv.reader(open(args.path_queries_ingredients, 'r', encoding="utf8"), delimiter="\t")
with open(args.path_result, 'w', encoding="utf8") as out:
    for query in queries:
        qid = query[0]
        out.write(f"{qid}\t{random.randint(7, 15)}\t{random.randint(7, 15)}\n")
