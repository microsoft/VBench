# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
import random
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--path-queries-ingredients', type=str, default="../vbench/queries/ingredients_keywords.tsv",
                    help='path to queries ingredients')
parser.add_argument('--path-result', type=str, default="../vbench/queries/and_filter.tsv",
                    help='path to save result')
args = parser.parse_args()

random.seed(0)
keywords = set()
queries = csv.reader(open(args.path_queries_ingredients, 'r', encoding="utf8"), delimiter="\t")
for query in queries:
    ingredients = query[1].split()
    keywords.update(ingredients)
print(f"Number of keyword in quereis: {len(keywords)}")

queries = csv.reader(open(args.path_queries_ingredients, 'r', encoding="utf8"), delimiter="\t")
with open(args.path_result, 'w', encoding="utf8") as out:
    for query in queries:
        qid = query[0]
        ingredients = query[1].split()
        # select 2 ingredients as filter
        if len(ingredients) > 1:
            word_in = random.sample(ingredients, 1)[0]
        else:
            word_in = random.sample(list(keywords), 1)[0]
        word_not_in = random.sample(list(keywords.difference(ingredients)), 1)[0]
        out.write(f"{qid}\t{word_in}\t{word_not_in}\n")
