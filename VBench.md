## Experimental setting

### Parameters.
* CPU: Intel(R) Xeon(R) CPU E5-2690 v3 @ 2.60GHz 2600 MHz
* OS: Linux Ubuntu 18.04 LTS
* GPU: Nvidia Tesla P100
* Memory: 112G

### Recipe1M Full Dataset

* Dataset Size: 340922
* Queries: 10000
* Collection Size: 330922
* Embedding Size (both images & instructions): 1024


## Elasticsearch

### Dense

| Engine        | Index | Metric | k   | k'   | Recall | Latency Mean / Std / 0.9 Tail Mean / 0.99 Tail Mean |
| ------------- | ----- | ------ | --- | ---- | ------ | --------------------------------------------------- |
| Elasticsearch | HNSW  | cosine | 50  | 256  | 0.9994 | 0.0745 / 0.0073 / 0.0907 / 0.1079                   |

### Dense + Or-Filter

| Engine        | Index | Metric | k   | k'   | Recall | Latency Mean / Std / 0.9 Tail Mean / 0.99 Tail Mean |
| ------------- | ----- | ------ | --- | ---- | ------ | --------------------------------------------------- |
| Elasticsearch | HNSW  | cosine | 50  | 256  | 0.4170 | 0.0748 / 0.0066 / 0.0855 / 0.0952                   |

### Dense + And-Filter

| Engine        | Index | Metric | k   | k'    | Recall  | Latency Mean / Std / 0.9 Tail Mean / 0.99 Tail Mean |
| ------------- | ----- | ------ | --- | ----- | ------- | --------------------------------------------------- |
| Elasticsearch | HNSW  | cosine | 50  | 10000 | 6.2e-05 | 0.0793 / 0.0127 / 0.1009 / 0.1121                   |

### Dense + Sparse

| Engine        | Index | Metric        | k   | k'   | Recall | Latency Mean / Std / 0.9 Tail Mean / 0.99 Tail Mean |
| ------------- | ----- | ------------- | --- | ---- | ------ | --------------------------------------------------- |
| Elasticsearch | HNSW  | cosine + BM25 | 50  | 256  | 0.7446 | 0.1382 / 0.0302 / 0.1936 / 0.2211                   |
| Elasticsearch | HNSW  | cosine + BM25 | 50  | 512  | 0.8488 | 0.1642 / 0.0398 / 0.2374 / 0.2744                   |
| Elasticsearch | HNSW  | cosine + BM25 | 50  | 1024 | 0.9173 | 0.2072 / 0.0545 / 0.3070 / 0.3559                   |
| Elasticsearch | HNSW  | cosine + BM25 | 50  | 2048 | 0.9445 | 0.2636 / 0.0759 / 0.4008 / 0.4662                   |
| Elasticsearch | HNSW  | cosine + BM25 | 50  | 4096 | 0.9472 | 0.2785 / 0.0847 / 0.4351 / 0.5207                   |
| Elasticsearch | HNSW  | cosine + BM25 | 50  | 8192 | 0.9472 | 0.2782 / 0.0845 / 0.4342 / 0.5198                   |

### Dense + Sparse + Or-Filter

| Engine        | Index | Metric        | k   | k'   | Recall | Latency Mean / Std / 0.9 Tail Mean / 0.99 Tail Mean |
| ------------- | ----- | ------------- | --- | ---- | ------ | --------------------------------------------------- |
| Elasticsearch | HNSW  | cosine + BM25 | 50  | 256  | 0.7273 | 0.1373 / 0.0295 / 0.1918 / 0.2193                   |
| Elasticsearch | HNSW  | cosine + BM25 | 50  | 512  | 0.8375 | 0.1628 / 0.0391 / 0.2353 / 0.2727                   |
| Elasticsearch | HNSW  | cosine + BM25 | 50  | 1024 | 0.9111 | 0.2037 / 0.0531 / 0.3015 / 0.3494                   |
| Elasticsearch | HNSW  | cosine + BM25 | 50  | 2048 | 0.9406 | 0.2565 / 0.0736 / 0.3912 / 0.4601                   |
| Elasticsearch | HNSW  | cosine + BM25 | 50  | 4096 | 0.9435 | 0.2698 / 0.0816 / 0.4222 / 0.5117                   |
| Elasticsearch | HNSW  | cosine + BM25 | 50  | 8192 | 0.9435 | 0.2697 / 0.0815 / 0.4222 / 0.5102                   |

### Dense + Sparse + And-Filter

| Engine        | Index | Metric        | k   | k'   | Recall | Latency Mean / Std / 0.9 Tail Mean / 0.99 Tail Mean |
| ------------- | ----- | ------------- | --- | ---- | ------ | --------------------------------------------------- |
| Elasticsearch | HNSW  | cosine + BM25 | 50  | 256  | 0.0310 | 0.0860 / 0.0290 / 0.1477 / 0.1801                   |
| Elasticsearch | HNSW  | cosine + BM25 | 50  | 512  | 0.0686 | 0.0930 / 0.0340 / 0.1666 / 0.2098                   |
| Elasticsearch | HNSW  | cosine + BM25 | 50  | 1024 | 0.1042 | 0.1056 / 0.0396 / 0.1936 / 0.2544                   |
| Elasticsearch | HNSW  | cosine + BM25 | 50  | 2048 | 0.1588 | 0.1207 / 0.0456 / 0.2238 / 0.3080                   |
| Elasticsearch | HNSW  | cosine + BM25 | 50  | 4096 | 0.1698 | 0.1245 / 0.0476 / 0.2317 / 0.3237                   |
| Elasticsearch | HNSW  | cosine + BM25 | 50  | 8192 | 0.1698 | 0.1249 / 0.0477 / 0.2325 / 0.3269                   |


## Milvus

### Dense

| Engine | Index    | nprobe | Metric        | Aggregation | k   | Recall | Latency Mean / Std / 0.9 Tail Mean / 0.99 Tail Mean |
| ------ | -------- | ------ | ------------- | ----------- | --- | ------ | --------------------------------------------------- |
| Milvus | IVF_FLAT | 1      | Inner Product | IMG (C++ )  | 50  | 0.7557 | 0.0012 / 0.0002 / 0.0015 / 0.0026                   |
| Milvus | IVF_FLAT | 2      | Inner Product | IMG (C++ )  | 50  | 0.8930 | 0.0012 / 0.0002 / 0.0014 / 0.0023                   |
| Milvus | IVF_FLAT | 3      | Inner Product | IMG (C++ )  | 50  | 0.9401 | 0.0011 / 0.0002 / 0.0014 / 0.0025                   |
| Milvus | IVF_FLAT | 4      | Inner Product | IMG (C++ )  | 50  | 0.9612 | 0.0011 / 0.0002 / 0.0014 / 0.0025                   |
| Milvus | IVF_FLAT | 5      | Inner Product | IMG (C++ )  | 50  | 0.9725 | 0.0011 / 0.0002 / 0.0014 / 0.0023                   |
| Milvus | IVF_FLAT | 8      | Inner Product | IMG (C++ )  | 50  | 0.9872 | 0.0014 / 0.0003 / 0.0018 / 0.0030                   |
| Milvus | IVF_FLAT | 16     | Inner Product | IMG (C++ )  | 50  | 0.9959 | 0.0014 / 0.0003 / 0.0018 / 0.0030                   |
| Milvus | IVF_FLAT | 32     | Inner Product | IMG (C++ )  | 50  | 0.9987 | 0.0013 / 0.0002 / 0.0017 / 0.0027                   |


### Dense + Or-filter

| Engine | Index    | nprobe | Metric        | Aggregation | k   | Recall | Latency Mean / Std / 0.9 Tail Mean / 0.99 Tail Mean |
| ------ | -------- | ------ | ------------- | ----------- | --- | ------ | --------------------------------------------------- |
| Milvus | IVF_FLAT | 1      | Inner Product | IMG (C++ )  | 50  | 0.7498 | 0.0012 / 0.0002 / 0.0016 / 0.0028                   |
| Milvus | IVF_FLAT | 2      | Inner Product | IMG (C++ )  | 50  | 0.8894 | 0.0012 / 0.0002 / 0.0015 / 0.0024                   |
| Milvus | IVF_FLAT | 3      | Inner Product | IMG (C++ )  | 50  | 0.9378 | 0.0012 / 0.0002 / 0.0015 / 0.0025                   |
| Milvus | IVF_FLAT | 4      | Inner Product | IMG (C++ )  | 50  | 0.9596 | 0.0012 / 0.0002 / 0.0016 / 0.0027                   |
| Milvus | IVF_FLAT | 5      | Inner Product | IMG (C++ )  | 50  | 0.9714 | 0.0012 / 0.0002 / 0.0016 / 0.0027                   |
| Milvus | IVF_FLAT | 8      | Inner Product | IMG (C++ )  | 50  | 0.9865 | 0.0014 / 0.0003 / 0.0018 / 0.0032                   |
| Milvus | IVF_FLAT | 16     | Inner Product | IMG (C++ )  | 50  | 0.9958 | 0.0014 / 0.0002 / 0.0018 / 0.0028                   |
| Milvus | IVF_FLAT | 32     | Inner Product | IMG (C++ )  | 50  | 0.9987 | 0.0014 / 0.0002 / 0.0017 / 0.0026                   |

### Multi Dense

| Engine | Index    | nlist | Metric        | Aggregation | k   | k'   | Recall | Latency Mean / Std / 0.9 Tail Mean / 0.99 Tail Mean |
| ------ | -------- | ----- | ------------- | ----------- | --- | ---- | ------ | --------------------------------------------------- |
| Milvus | IVF_FLAT | 1024  | Inner Product | IMG (C++ )  | 50  | 256  | 0.2700 | 0.1544 / 0.0092 / 0.1647 / 0.1727                   |
| Milvus | IVF_FLAT | 1024  | Inner Product | IMG (C++ )  | 50  | 512  | 0.3907 | 0.5833 / 0.0788 / 0.6367 / 0.6764                   |
| Milvus | IVF_FLAT | 1024  | Inner Product | IMG (C++ )  | 50  | 1024 | 0.5610 | 2.0754 / 0.6067 / 2.4854 / 2.5199                   |
| Milvus | IVF_FLAT | 1024  | Inner Product | IMG (C++ )  | 50  | 2048 | 0.6754 | 6.3849 / 3.5095 / 9.9831 / 10.1072                  |
| Milvus | IVF_FLAT | 1024  | Inner Product | IMG (C++ )  | 50  | 4096 | 0.7441 | 15.9408 / 15.0971 / 40.1692 / 40.7554               |
| Milvus | IVF_FLAT | 2048  | Inner Product | IMG (C++ )  | 50  | 256  | 0.3763 | 0.1541 / 0.0072 / 0.1634 / 0.1715                   |
| Milvus | IVF_FLAT | 2048  | Inner Product | IMG (C++ )  | 50  | 512  | 0.5382 | 0.5888 / 0.0570 / 0.6308 / 0.6458                   |
| Milvus | IVF_FLAT | 2048  | Inner Product | IMG (C++ )  | 50  | 1024 | 0.6877 | 2.1534 / 0.5023 / 2.4810 / 2.5154                   |
| Milvus | IVF_FLAT | 2048  | Inner Product | IMG (C++ )  | 50  | 2048 | 0.8087 | 7.0795 / 3.2655 / 9.9945 / 10.1472                  |
| Milvus | IVF_FLAT | 2048  | Inner Product | IMG (C++ )  | 50  | 4096 | 0.8846 | 20.1531 / 15.5922 / 40.2994 / 40.7204               |
| Milvus | IVF_FLAT | 4096  | Inner Product | IMG (C++ )  | 50  | 256  | 0.4553 | 0.1535 / 0.0070 / 0.1630 / 0.1720                   |
| Milvus | IVF_FLAT | 4096  | Inner Product | IMG (C++ )  | 50  | 512  | 0.6135 | 0.5882 / 0.0545 / 0.6305 / 0.6476                   |
| Milvus | IVF_FLAT | 4096  | Inner Product | IMG (C++ )  | 50  | 1024 | 0.7629 | 2.1757 / 0.4828 / 2.4893 / 2.5329                   |
| Milvus | IVF_FLAT | 4096  | Inner Product | IMG (C++ )  | 50  | 2048 | 0.8714 | 7.2214 / 3.1835 / 9.9823 / 10.1036                  |
| Milvus | IVF_FLAT | 4096  | Inner Product | IMG (C++ )  | 50  | 4096 | 0.9314 | 20.8948 / 15.5378 / 40.3540 / 40.8074               |


### Multi Dense + Or-Filter

| Engine | Index    | nlist | Metric        | Aggregation | k   | k'   | Recall | Latency Mean / Std / 0.9 Tail Mean / 0.99 Tail Mean |
| ------ | -------- | ----- | ------------- | ----------- | --- | ---- | ------ | --------------------------------------------------- |
| Milvus | IVF_FLAT | 1024  | Inner Product | IMG (C++ )  | 50  | 256  | 0.2713 | 0.1523 / 0.0136 / 0.1654 / 0.1747                   |
| Milvus | IVF_FLAT | 1024  | Inner Product | IMG (C++ )  | 50  | 512  | 0.3884 | 0.5717 / 0.0885 / 0.6340 / 0.6502                   |
| Milvus | IVF_FLAT | 1024  | Inner Product | IMG (C++ )  | 50  | 1024 | 0.5515 | 1.9987 / 0.6612 / 2.4907 / 2.5492                   |
| Milvus | IVF_FLAT | 1024  | Inner Product | IMG (C++ )  | 50  | 2048 | 0.6546 | 5.9148 / 3.6308 / 10.0695 / 10.3974                 |
| Milvus | IVF_FLAT | 1024  | Inner Product | IMG (C++ )  | 50  | 4096 | 0.6740 | 17.8238 / 15.7955 / 41.2953 / 44.7126               |
| Milvus | IVF_FLAT | 2048  | Inner Product | IMG (C++ )  | 50  | 256  | 0.3781 | 0.1552 / 0.0079 / 0.1654 / 0.1764                   |
| Milvus | IVF_FLAT | 2048  | Inner Product | IMG (C++ )  | 50  | 512  | 0.5389 | 0.5902 / 0.0607 / 0.6340 / 0.6499                   |
| Milvus | IVF_FLAT | 2048  | Inner Product | IMG (C++ )  | 50  | 1024 | 0.6868 | 2.1418 / 0.5287 / 2.4971 / 2.5319                   |
| Milvus | IVF_FLAT | 2048  | Inner Product | IMG (C++ )  | 50  | 2048 | 0.8054 | 6.9293 / 3.3885 / 10.1035 / 10.4009                 |
| Milvus | IVF_FLAT | 2048  | Inner Product | IMG (C++ )  | 50  | 4096 | 0.8451 | 22.7197 / 16.0949 / 41.8324 / 44.7971               |
| Milvus | IVF_FLAT | 4096  | Inner Product | IMG (C++ )  | 50  | 256  | 0.4620 | 0.1554 / 0.0073 / 0.1653 / 0.1731                   |
| Milvus | IVF_FLAT | 4096  | Inner Product | IMG (C++ )  | 50  | 512  | 0.6191 | 0.5921 / 0.0574 / 0.6371 / 0.6586                   |
| Milvus | IVF_FLAT | 4096  | Inner Product | IMG (C++ )  | 50  | 1024 | 0.7667 | 2.1714 / 0.5013 / 2.5052 / 2.5455                   |
| Milvus | IVF_FLAT | 4096  | Inner Product | IMG (C++ )  | 50  | 2048 | 0.8732 | 7.1297 / 3.2882 / 10.1215 / 10.5605                 |
| Milvus | IVF_FLAT | 4096  | Inner Product | IMG (C++ )  | 50  | 4096 | 0.9015 | 23.6241 / 15.8189 / 41.9496 / 44.9304               |