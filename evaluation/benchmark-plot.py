# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

ylabels_show = {
    'Latency': 'Average Latency',
    '09TailLatency': '0.9 Tail Latency',
    '099TailLatency': '0.99 Tail Latency'
}

def plot_milvus(single=True, multi=True):
    ylabels = ["Latency", "099TailLatency"]
    if single and not multi:
        df0 = pd.read_csv('./result/summary/single/milvus.csv')
        df1 = pd.read_csv('./result/summary/single/milvus-or.csv')
        df = pd.concat([df0, df1], axis=0)
    elif not single and multi:
        df0 = pd.read_csv('./result/summary/milvus.csv')
        df1 = pd.read_csv('./result/summary/milvus-or.csv')
        df = pd.concat([df0, df1], axis=0)
    if single and multi:
        df0 = pd.read_csv('./result/summary/single/milvus.csv')
        df1 = pd.read_csv('./result/summary/single/milvus-or.csv')
        df2 = pd.read_csv('./result/summary/milvus.csv')
        df3 = pd.read_csv('./result/summary/milvus-or.csv')
        df = pd.concat([df0, df1, df2, df3], axis=0)

    df["Latency"] = df["Latency"] * 1000
    df["09TailLatency"] = df["09TailLatency"] * 1000
    df["099TailLatency"] = df["099TailLatency"] * 1000

    df = pd.melt(df, id_vars=['Query', 'kPrime', 'Recall'], value_vars=ylabels, var_name='latency-type', value_name='Latency (ms)')

    df = df.replace('Q2', 'Q2, No Filter')
    df = df.replace('Q5', 'Q5, Numeric Filter')

    g = sns.FacetGrid(df, col="latency-type", margin_titles=False)
    g.map_dataframe(sns.lineplot, x="Recall", y="Latency (ms)", hue="Query", style="Query", markers=['s', 'o'])
    # g.add_legend()
    g.axes[0,0].legend()
    g.axes[0,0].set_xlabel('Recall@50')
    g.axes[0,1].set_xlabel('Recall@50')

    axes = g.axes.flatten()
    for i, ylabel in enumerate(ylabels):
        axes[i].set_title(ylabels_show[ylabel])
    plt.savefig("./result/summary/img/milvus.png")
    plt.savefig("./result/summary/img/milvus.pdf")

def plot_es(single=False):
    ylabels = ["Latency", "099TailLatency"]
    if single:
        df2 = pd.read_csv('./result/summary/single/es.csv')
        # df3 = pd.read_csv('./result/summary/single/es-or.csv')
        df4 = pd.read_csv('./result/summary/single/es-and.csv')
        df = pd.concat([df2,  df4], axis=0)# df3,
        df = df.replace('Q1', 'Q1, No Filter')
        df = df.replace('Q4', 'Q4, Numeric Filter')
        df = df.replace('Q7', 'Q7, String Filter')
    else:
        df2 = pd.read_csv('./result/summary/es.csv')
        df3 = pd.read_csv('./result/summary/es-or.csv')
        df4 = pd.read_csv('./result/summary/es-and.csv')
        df = pd.concat([df2, df3, df4], axis=0)
        df = df.replace('Q3', 'Q3, No Filter')
        df = df.replace('Q6', 'Q6, Numeric Filter')
        df = df.replace('Q9', 'Q9, String Filter')

    df = pd.melt(df, id_vars=['Query', 'kprime', 'Recall'], value_vars=ylabels, var_name='latency-type', value_name='Latency (ms)')
    
    g = sns.FacetGrid(df, col="latency-type", margin_titles=True) # aspect=0.75,
    g.map_dataframe(sns.lineplot, x="Recall", y="Latency (ms)", hue="Query", style="Query", markers=['s', 'o', '^'])
    g.axes[0,0].legend()
    g.axes[0,0].set_xlabel('Recall@50')
    g.axes[0,1].set_xlabel('Recall@50')

    axes = g.axes.flatten()
    for i, ylabel in enumerate(ylabels):
        axes[i].set_title(ylabels_show[ylabel])
    if single:
        file_name = "es-single"
    else:
        file_name = "es-multi"
    plt.savefig(f"./result/summary/img/{file_name}.png")
    plt.savefig(f"./result/summary/img/{file_name}.pdf")

def plot_join():
    df = pd.read_csv('./result/summary/join.csv')
    sns.lineplot(data=df, x="size", y="latency")

    plt.savefig(f"./result/summary/img/join.png")
    plt.savefig(f"./result/summary/img/join.pdf")

def plot_ranger():
    ylabels = ["Latency", "099TailLatency"]
    df = pd.read_csv('./result/summary/ranger.csv')
    df = pd.melt(df, id_vars=['size', 'Query', 'Recall'], value_vars=ylabels, var_name='latency-type', value_name='Latency (ms)')

    g = sns.FacetGrid(df, col="latency-type", margin_titles=True) # aspect=0.75,
    g.map_dataframe(sns.lineplot, x="Recall", y="Latency (ms)", hue="Query", style="Query", markers=['s'])#.set(yscale = 'log')
    g.axes[0,0].legend()
    g.axes[0,0].set_xlabel('Recall@50')
    g.axes[0,1].set_xlabel('Recall@50')

    axes = g.axes.flatten()
    for i, ylabel in enumerate(ylabels):
        axes[i].set_title(ylabels_show[ylabel])

    plt.savefig(f"./result/summary/img/ranger.png")
    plt.savefig(f"./result/summary/img/ranger.pdf")

if __name__ == "__main__":
    plot_milvus(False, True)
    # plot_es(single=True)
    plot_es()
    # plot_join()
    plot_ranger()
