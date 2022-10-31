# cd Recipe1M

PATH_COLLECTION="./vbench/collections/10k/"
PATH_QUERY="./vbench/queries/"
PATH_RESULT="./vbench/exact/10k/"

# dense
python get-dense-exact-result.py \
--filter 'no' \
--k 50 \
--log-frequency 100 \
--path-img-embeddings "${PATH_COLLECTION}img_embeds_collection.tsv" \
--path-number-data "${PATH_COLLECTION}numbers.tsv" \
--path-text-data "${PATH_COLLECTION}text.tsv" \
--path-img-queries "${PATH_QUERY}img_embeds_query.tsv" \
--path-query-filter "${PATH_QUERY}or_filter.tsv" \
--path-results "${PATH_RESULT}dense-top50.tsv" \
--start-line 0 \
--end-line 10000

# dense + or filterdense
python get-dense-exact-result.py \
--filter 'or' \
--k 50 \
--log-frequency 100 \
--path-img-embeddings "${PATH_COLLECTION}img_embeds_collection.tsv" \
--path-number-data "${PATH_COLLECTION}numbers.tsv" \
--path-text-data "${PATH_COLLECTION}text.tsv" \
--path-img-queries "${PATH_QUERY}img_embeds_query.tsv" \
--path-query-filter "${PATH_QUERY}or_filter.tsv" \
--path-results "${PATH_RESULT}dense-or-top50.tsv" \
--start-line 0 \
--end-line 10000

# dense + and filter
python get-dense-exact-result.py \
--filter 'and' \
--k 50 \
--log-frequency 100 \
--path-img-embeddings "${PATH_COLLECTION}img_embeds_collection.tsv" \
--path-number-data "${PATH_COLLECTION}numbers.tsv" \
--path-text-data "${PATH_COLLECTION}text.tsv" \
--path-img-queries "${PATH_QUERY}img_embeds_query.tsv" \
--path-query-filter "${PATH_QUERY}and_filter.tsv" \
--path-results "${PATH_RESULT}dense-and-top50.tsv" \
--start-line 0 \
--end-line 10000

# multi vector + no filter
python get-multi-dense-filter-exact-result.py \
--filter 'no' \
--k 50 \
--log-frequency 100 \
--path-img-embeddings "${PATH_COLLECTION}img_embeds_collection.tsv" \
--path-text-embeddings "${PATH_COLLECTION}rec_embeds_collection.tsv" \
--path-number-data "${PATH_COLLECTION}numbers.tsv" \
--path-text-data "${PATH_COLLECTION}text.tsv" \
--path-img-queries "${PATH_QUERY}img_embeds_query.tsv" \
--path-text-queries "${PATH_QUERY}rec_embeds_query.tsv" \
--path-query-filter "${PATH_QUERY}or_filter.tsv" \
--path-results "${PATH_RESULT}qrels-multi-dense-no-filter-exact-top50.tsv" \
--start-line 0 \
--end-line 10000

# multi vector + or filter
python get-multi-dense-filter-exact-result.py \
--filter 'or' \
--k 50 \
--log-frequency 100 \
--path-img-embeddings "${PATH_COLLECTION}img_embeds_collection.tsv" \
--path-text-embeddings "${PATH_COLLECTION}rec_embeds_collection.tsv" \
--path-number-data "${PATH_COLLECTION}numbers.tsv" \
--path-text-data "${PATH_COLLECTION}text.tsv" \
--path-img-queries "${PATH_QUERY}img_embeds_query.tsv" \
--path-text-queries "${PATH_QUERY}rec_embeds_query.tsv" \
--path-query-filter "${PATH_QUERY}or_filter.tsv" \
--path-results "${PATH_RESULT}qrels-multi-dense-or-filter-exact-top50.tsv" \
--start-line 0 \
--end-line 10000

# multi vector + and filter
python get-multi-dense-filter-exact-result.py \
--filter 'and' \
--k 50 \
--log-frequency 100 \
--path-img-embeddings "${PATH_COLLECTION}img_embeds_collection.tsv" \
--path-text-embeddings "${PATH_COLLECTION}rec_embeds_collection.tsv" \
--path-number-data "${PATH_COLLECTION}numbers.tsv" \
--path-text-data "${PATH_COLLECTION}text.tsv" \
--path-img-queries "${PATH_QUERY}img_embeds_query.tsv" \
--path-text-queries "${PATH_QUERY}rec_embeds_query.tsv" \
--path-query-filter "${PATH_QUERY}and_filter.tsv" \
--path-results "${PATH_RESULT}multi-dense-and-filter-exact-top50.tsv" \
--start-line 0 \
--end-line 10000

# dense + sparse
python get-dense-sparse-exact-result.py \
--filter 'no' \
--path-query-text "${PATH_QUERY}text.tsv" \
--path-query-embeds "${PATH_QUERY}img_embeds_query.tsv" \
--inverted-index-key "text" \
--knn-key "embeds_image" \
--knn-weight 50 --k 50 \
--path-exact-result "${PATH_RESULT}dense-sparse-top50.tsv"

# dense + sparse + or filter
python get-dense-sparse-exact-result.py \
--filter 'or' \
--path-query-embeds "${PATH_QUERY}img_embeds_query.tsv" \
--path-query-text "${PATH_QUERY}text.tsv" \
--path-query-filter "${PATH_QUERY}or_filter.tsv" \
--inverted-index-key "text" \
--knn-key "embeds_image" \
--knn-weight 50 --k 50 \
--path-exact-result "${PATH_RESULT}dense-sparse-or-top50.tsv"

# dense + sparse + and filter
python get-dense-sparse-exact-result.py \
--filter 'and' \
--path-query-embeds "${PATH_QUERY}img_embeds_query.tsv" \
--path-query-text "${PATH_QUERY}text.tsv" \
--path-query-filter "${PATH_QUERY}and_filter.tsv" \
--inverted-index-key "text" \
--knn-key "embeds_image" \
--knn-weight 50 --k 50 \
--path-exact-result "${PATH_RESULT}dense-sparse-and-top50.tsv"
