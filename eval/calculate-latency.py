# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
import argparse
import statistics
import ast
import pandas as pd

def calculate_latency(path):
    res_latency = pd.read_csv(path, delimiter='\t')
    latency = res_latency.iloc[:, 1].tolist()
    latency.sort()

    latency = [i * 1000 for i in latency] # to ms
    print(" Latency mean / std / Tail Latency 0.9 / 0.99 (ms):")
    print(f"{statistics.mean(latency):.1f},{statistics.stdev(latency):.1f},{statistics.mean(latency[int(0.9*len(latency)):]):.1f},{statistics.mean(latency[int(0.99*len(latency)):]):.1f}")

    if len(res_latency.columns) <= 2:
        return
    details = res_latency.iloc[:, 2].tolist()
    iterations = [len(ast.literal_eval(detail)) for detail in details]
    vec0_latencies = [sum(t[0] for t in ast.literal_eval(detail)) for detail in details]
    vec1_latencies = [sum(t[1] for t in ast.literal_eval(detail)) for detail in details]
    NRA_latencies = [sum(t[2] for t in ast.literal_eval(detail)) for detail in details]
    NRA_succeeded = res_latency.iloc[:, 3].tolist()
    rows = res_latency.iloc[:, 4].tolist()

    print(f"Number of IMG iterations mean / std (s): {statistics.mean(iterations):.4f} / {statistics.stdev(iterations):.4f}")
    print(f"Vector 0 latency mean / std (s): {statistics.mean(vec0_latencies):.4f} / {statistics.stdev(vec0_latencies):.4f}")
    print(f"Vector 1 latency mean / std (s): {statistics.mean(vec1_latencies):.4f} / {statistics.stdev(vec0_latencies):.4f}")
    print(f"NRA latency mean / std (s): {statistics.mean(NRA_latencies):.4f} / {statistics.stdev(vec0_latencies):.4f}")
    print(f"Proportion NRA succeeded : {statistics.mean(NRA_succeeded):.4f}")
    print(f"Max visited rows mean / std (s): {statistics.mean(rows):.4f} / {statistics.stdev(rows):.4f}")

if  __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--path-latency-result', type=str, default='../result/Recipe1M/test-qrels-latency-top50-nprobe8-limit1024.tsv',
                        help='path to latency result')

    args = parser.parse_args()
    calculate_latency(args.path_latency_result)
