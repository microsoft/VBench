# cd Recipe1M

PATH_COLLECTION="./vbench/collections/"
PATH_QUERY="./vbench/queries/"
PATH_RESULT="./vbench/exact/"
# PATH_COLLECTION="./vbench/collections/10k/"
# PATH_RESULT="./vbench/exact/10k/"

# Q1
python get_dense_exact_result.py \
--filter 'no' \
--k 50 \
--log-frequency 100 \
--path-img-embeddings "${PATH_COLLECTION}img_embeds.tsv" \
--path-img-queries "${PATH_QUERY}img_embeds.tsv" \
--path-query-filter "${PATH_QUERY}price.tsv" \
--path-results "${PATH_RESULT}q1.tsv" \
--start-line 0 \
--end-line 10000

# Q4
# python get_dense_exact_result.py \
# --filter 'number' \
# --k 50 \
# --log-frequency 100 \
# --path-img-embeddings "${PATH_COLLECTION}img_embeds.tsv" \
# --path-number-data "${PATH_COLLECTION}price.tsv" \
# --path-img-queries "${PATH_QUERY}img_embeds.tsv" \
# --path-query-filter "${PATH_QUERY}price.tsv" \
# --path-results "${PATH_RESULT}q4.tsv" \
# --start-line 0 \
# --end-line 10000

# Q7
# python get_dense_exact_result.py \
# --filter 'string' \
# --k 50 \
# --log-frequency 100 \
# --path-img-embeddings "${PATH_COLLECTION}img_embeds.tsv" \
# --path-text-data "${PATH_COLLECTION}text.tsv" \
# --path-img-queries "${PATH_QUERY}img_embeds.tsv" \
# --path-query-filter "${PATH_QUERY}string_filter.tsv" \
# --path-results "${PATH_RESULT}q7.tsv" \
# --start-line 0 \
# --end-line 10000

# Q2
python get_multi_dense_exact_result.py \
--filter 'no' \
--k 50 \
--log-frequency 100 \
--path-img-embeddings "${PATH_COLLECTION}img_embeds.tsv" \
--path-text-embeddings "${PATH_COLLECTION}rec_embeds.tsv" \
--path-img-queries "${PATH_QUERY}img_embeds.tsv" \
--path-text-queries "${PATH_QUERY}rec_embeds.tsv" \
--path-query-filter "${PATH_QUERY}price.tsv" \
--path-results "${PATH_RESULT}q2.tsv" \
--start-line 0 \
--end-line 10000

# Q5
# python get_multi_dense_exact_result.py \
# --filter 'number' \
# --k 50 \
# --log-frequency 100 \
# --path-img-embeddings "${PATH_COLLECTION}img_embeds.tsv" \
# --path-text-embeddings "${PATH_COLLECTION}rec_embeds.tsv" \
# --path-number-data "${PATH_COLLECTION}price.tsv" \
# --path-img-queries "${PATH_QUERY}img_embeds.tsv" \
# --path-text-queries "${PATH_QUERY}rec_embeds.tsv" \
# --path-query-filter "${PATH_QUERY}price.tsv" \
# --path-results "${PATH_RESULT}q5.tsv" \
# --start-line 0 \
# --end-line 10000

# # Q8
# python get_multi_dense_exact_result.py \
# --filter 'string' \
# --k 50 \
# --log-frequency 100 \
# --path-img-embeddings "${PATH_COLLECTION}img_embeds.tsv" \
# --path-text-embeddings "${PATH_COLLECTION}rec_embeds.tsv" \
# --path-text-data "${PATH_COLLECTION}text.tsv" \
# --path-img-queries "${PATH_QUERY}img_embeds.tsv" \
# --path-text-queries "${PATH_QUERY}rec_embeds.tsv" \
# --path-query-filter "${PATH_QUERY}string_filter.tsv" \
# --path-results "${PATH_RESULT}q8.tsv" \
# --start-line 0 \
# --end-line 10000

# Q3
# python get_dense_sparse_exact_result.py \
# --filter 'no' \
# --path-query-text "${PATH_QUERY}text.tsv" \
# --path-query-embeds "${PATH_QUERY}img_embeds.tsv" \
# --inverted-index-key "text" \
# --knn-key "embeds_image" \
# --knn-weight 50 --k 50 \
# --path-exact-result "${PATH_RESULT}q3.tsv"

# # Q6
# python get_dense_sparse_exact_result.py \
# --filter 'number' \
# --path-query-embeds "${PATH_QUERY}img_embeds.tsv" \
# --path-query-text "${PATH_QUERY}text.tsv" \
# --path-query-filter "${PATH_QUERY}price.tsv" \
# --inverted-index-key "text" \
# --knn-key "embeds_image" \
# --knn-weight 50 --k 50 \
# --path-exact-result "${PATH_RESULT}q6.tsv"

# # Q9
# python get_dense_sparse_exact_result.py \
# --filter 'string' \
# --path-query-embeds "${PATH_QUERY}img_embeds.tsv" \
# --path-query-text "${PATH_QUERY}text.tsv" \
# --path-query-filter "${PATH_QUERY}string_filter.tsv" \
# --inverted-index-key "text" \
# --knn-key "embeds_image" \
# --knn-weight 50 --k 50 \
# --path-exact-result "${PATH_RESULT}q9.tsv"
