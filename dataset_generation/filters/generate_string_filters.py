# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
import random
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--path-queries-ingredients', type=str, default="../vbench/queries/keywords.tsv",
                    help='path to queries ingredients')
parser.add_argument('--path-result', type=str, default="../vbench/queries/string_filter.tsv",
                    help='path to save result')
args = parser.parse_args()

random.seed(0)
keywords = []
queries = csv.reader(open(args.path_queries_ingredients, 'r', encoding="utf8"), delimiter="\t")
for query in queries:
    ingredients = query[1].split()
    keywords.extend(ingredients)
print(f"Number of keywords in queries: {len(keywords)}")
print(keywords[:10])

queries = csv.reader(open(args.path_queries_ingredients, 'r', encoding="utf8"), delimiter="\t")
with open(args.path_result, 'w', encoding="utf8") as out:
    for query in queries:
        qid = query[0]
        ingredients = query[1].split()
        word_not_in = random.sample(keywords, 1)[0]
        out.write(f"{qid}\t{word_not_in}\n")
