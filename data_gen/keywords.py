# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
import os
import argparse
import pickle
import random
import lmdb
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--vocab', dest='vocab', default='../data/vocab.txt')
parser.add_argument('--lmdb', dest='lmdb', default='../data')
parser.add_argument('--partition', dest='partition', default='query')
parser.add_argument('--path-result-keywords', type=str, default="../data/queries/keywords.tsv",
                    help='path to save result')
parser.add_argument('--path-result-numbers', type=str, default="../data/queries/numbers.tsv",
                    help='path to save result')
opts = parser.parse_args()

# ingredients vector to string
with open(opts.vocab) as f_vocab:
    ingr_vocab = {w.rstrip(): i+2 for i, w in enumerate(f_vocab)}  # +1 for lua
    ingr_vocab['</i>'] = 1
    vocab_key = list(ingr_vocab.keys())
    vocab_value = list(ingr_vocab.values())

def get_dict_key(value):
    idx = vocab_value.index(value)
    return vocab_key[idx]

# Open lmdb
env_test = lmdb.open(os.path.join(opts.lmdb, 'test/test_lmdb'), map_size=int(1e11))
env_val = lmdb.open(os.path.join(opts.lmdb, 'val/val_lmdb'), map_size=int(1e11))
env_train = lmdb.open(os.path.join(opts.lmdb, 'train/train_lmdb'), map_size=int(1e11))
env_list = [env_test, env_val, env_train]

with open(os.path.join(opts.lmdb, 'train/train_keys.pkl'), 'rb') as f:
    train_ids = pickle.load(f)
with open(os.path.join(opts.lmdb, 'val/val_keys.pkl'), 'rb') as f:
    val_ids = pickle.load(f)
with open(os.path.join(opts.lmdb, 'test/test_keys.pkl'), 'rb') as f:
    test_ids = pickle.load(f)
ids_list = [test_ids, val_ids, train_ids]

SIZE_QUERY = 10000
SIZE_COLLECTION = len(test_ids)+len(val_ids)+len(train_ids)-SIZE_QUERY
random.seed(0)
ids = list(range(SIZE_COLLECTION+SIZE_QUERY))
qids = random.sample(ids, SIZE_QUERY)

ids = [ids[:len(test_ids)], ids[len(test_ids):len(test_ids)+len(val_ids)], ids[len(test_ids)+len(val_ids):]]
minus = [0, len(test_ids), len(test_ids)+len(val_ids)]
target_idlist = [[], [], []]
for num in range(len(target_idlist)):
    for index in ids[num]:
        if opts.partition == 'query' and index in qids or opts.partition == 'collection' and index not in qids:
            target_idlist[num].append(index-minus[num])

with open(opts.path_result_keywords, 'w', encoding="utf8") as out_keywords, \
    open(opts.path_result_numbers, 'w', encoding="utf8") as out_numbers:
    for num in range(len(target_idlist)):
        for index in target_idlist[num]:
            origin_index = ids_list[num][index]
            with env_list[num].begin(write=False) as txn:
                serialized_sample = txn.get(origin_index.encode('latin1'))
            sample = pickle.loads(serialized_sample, encoding='latin1')

            instructions = sample['intrs']
            ingredients = []
            for idx in sample['ingrs'].astype(int):
                if idx > 1:
                    ingredients.append(get_dict_key(idx))
                else:
                    break   

            out_keywords.write(f"{index+minus[num]}\t{' '.join(ingredients)}\n")
            out_numbers.write(f"{index+minus[num]}\t{len(ingredients)}\t{len(instructions)}\n")
