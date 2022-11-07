# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
import json
import random
import pickle
import argparse
import os
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--lmdb', dest='lmdb', default='../data')
parser.add_argument('--json', dest='json', default='../data/layer1.json')
parser.add_argument('--partition', dest='partition', default='query')
parser.add_argument('--path-result', type=str, default="../vbench/queries/ingredients_keywords.tsv",
                    help='path to save result')
opts = parser.parse_args()

with open(os.path.join(opts.lmdb, 'test/test_keys.pkl'), 'rb') as f:
    test_ids = pickle.load(f)
with open(os.path.join(opts.lmdb, 'val/val_keys.pkl'), 'rb') as f:
    val_ids = pickle.load(f)
with open(os.path.join(opts.lmdb, 'train/train_keys.pkl'), 'rb') as f:
    train_ids = pickle.load(f)
index = np.concatenate((test_ids, val_ids, train_ids))

print("Reading json...")
data = {}
with open(opts.json, 'r') as f:
    jsondata = json.load(f)
    for recipe in jsondata:
        data[recipe['id']] = {
            'ingredients': ' '.join([x['text'] for x in recipe['ingredients']]),
            'instructions': ' '.join([x['text'] for x in recipe['instructions']])
        }

print("Writing tsv...")
SIZE_QUERY = 10000
SIZE_COLLECTION = len(index)-SIZE_QUERY
random.seed(0)
ids = list(range(len(index)))
qids = sorted(random.sample(ids, SIZE_QUERY))

target_ids = []
if opts.partition == 'query':
    target_ids = qids
elif opts.partition == 'collection':
    target_ids = [tid for tid in ids if tid not in qids]

with open(opts.path_result, 'w', encoding="utf8") as out:
    for tid in target_ids:
        text = data[index[tid]]
        out.write(f"{tid}\t{text['ingredients']}\t{text['instructions']}\n")
