# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
import argparse
import pandas as pd

if  __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # parser.add_argument('--k', type=int, default=10,
    #                     help='top k')
    parser.add_argument('--path-search-results', type=str, default="../result/Recipe1M/test-qrels-top50-nprobe16-limit4096.tsv",
                        help='path to embedding result')
    parser.add_argument('--path-exact-results', type=str, default="../result/Recipe1M/test-qrels-exact-top50.tsv",
                        help='path to embedding result')
    args = parser.parse_args()

    df_qrels = pd.read_csv(args.path_search_results, header=None, delimiter='\t')
    df_qrels.columns = ['qid', 'number']

    total = 0.001783909392543137 * 330922 * 10000

    print(f"recall : {sum(df_qrels['number'].tolist())/total:.4f}")
