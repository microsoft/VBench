PATH_RESULT="../result/10k/ElasticSearch"
PATH_EXACT_RESULT="../Recipe1M/vbench/exact/10k"

for k in 256 # 512 1024 2048 4096 8192 10000
do
    python eval/calculate-recall.py \
    --path-search-results ${PATH_RESULT}/dense-and-post/qrels-${k}.tsv \
    --path-exact-results ${PATH_EXACT_RESULT}/dense-and-top50.tsv
done

# for k in 256 512 1024 2048 4096 8192 10000
# do
#     python eval/calculate-latency.py \
#     --path-latency-result ${PATH_RESULT}/dense-and-post/latency-${k}.tsv
# done

# for k in 256 512 1024 2048 4096 8192 10000
# do
#     python eval/calculate-recall.py \
#     --path-search-results ${PATH_RESULT}/dense-or-post/qrels-${k}.tsv \
#     --path-exact-results ${PATH_EXACT_RESULT}/dense-or-top50.tsv
# done

# for k in 256 512 1024 # 2048 4096 8192 # 10000
# do
#     python eval/calculate-latency.py \
#     --path-latency-result ${PATH_RESULT}/dense-or-post/latency-${k}.tsv
# done

# 213.6,49.6,297.2,332.6
# python eval/calculate-latency.py \
# --path-latency-result ${PATH_RESULT}/sparse/latency.tsv

# 574.6,224.7,997.0,1193.9
# python eval/calculate-latency.py \
# --path-latency-result ${PATH_RESULT}/sparse-or/latency.tsv

# 335.4,187.7,696.7,903.7
# python eval/calculate-latency.py \
# --path-latency-result ${PATH_RESULT}/sparse-and/latency.tsv
