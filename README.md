## Recipe1M Embedding

### Get Recipe1M Dataset Embeddings

* Run `get-embedding.sh`, 
* The results will be saved in `im2recipe-Pytorch/results`

Notes: We use model `model_e220_v-4.700.pth.tar` , which should be better than model_e500_v-8.950.pth.tar

### Split Embedding Results

```bash
# `img_embeds_query.tsv`: size 5133
# `rec_embeds_query.tsv`: size 5133
# `img_embeds_collection.tsv`: size 46201
# `rec_embeds_collection.tsv`: size 46201
echo "Splitting test embedding..."
mkdir -p embedding/test-split
python split_embedding.py  \
--path-embeddings "im2recipe-Pytorch/results/test" \
--path-results "embedding/test-split"

echo "Splitting all embedding..."
# `img_embeds_query.tsv`: size 10000
# `rec_embeds_query.tsv`: size 10000
# `img_embeds_collection.tsv`: size 330922
# `rec_embeds_collection.tsv`: size 330922
mkdir -p embedding/split
python split_embedding.py  \
--path-embeddings "im2recipe-Pytorch/results/test" "im2recipe-Pytorch/results/val" "im2recipe-Pytorch/results/train" \
--path-results "embedding/split" \
--queries 10000

echo "Getting subcollection (10k)..."
python get_sub_collection.py
```

### Exact Results

```bash
cd Recipe1M

# dense
python get-dense-exact-result.py \
--filter 'no' \
--k 50 \
--log-frequency 100 \
--path-img-embeddings "./vbench/collections/img_embeds_collection.tsv" \
--path-number-data "./vbench/collections/numbers.tsv" \
--path-text-data "./vbench/collections/text.tsv" \
--path-img-queries "./vbench/queries/img_embeds_query.tsv" \
--path-query-filter "./vbench/queries/or_filter.tsv" \
--path-results "./vbench/exact/dense-top50.tsv"

# dense + or filterdense
python get-dense-exact-result.py \
--filter 'or' \
--k 50 \
--log-frequency 100 \
--path-img-embeddings "./vbench/collections/img_embeds_collection.tsv" \
--path-number-data "./vbench/collections/numbers.tsv" \
--path-text-data "./vbench/collections/text.tsv" \
--path-img-queries "./vbench/queries/img_embeds_query.tsv" \
--path-query-filter "./vbench/queries/or_filter.tsv" \
--path-results "./vbench/exact/dense-or-top50.tsv"

# dense + and filter
python get-dense-exact-result.py \
--filter 'and' \
--k 50 \
--log-frequency 100 \
--path-img-embeddings "./vbench/collections/img_embeds_collection.tsv" \
--path-number-data "./vbench/collections/numbers.tsv" \
--path-text-data "./vbench/collections/text.tsv" \
--path-img-queries "./vbench/queries/img_embeds_query.tsv" \
--path-query-filter "./vbench/queries/and_filter.tsv" \
--path-results "./vbench/exact/dense-and-top50.tsv"

# multi vector + no filter
python get-multi-dense-filter-exact-result.py \
--filter 'no' \
--k 50 \
--log-frequency 100 \
--path-img-embeddings "./vbench/collections/img_embeds_collection.tsv" \
--path-embeds-text "./vbench/collections/rec_embeds_collection.tsv" \
--path-number-data "./vbench/collections/numbers.tsv" \
--path-text-data "./vbench/collections/text.tsv" \
--path-img-queries "./vbench/queries/img_embeds_query.tsv" \
--path-text-queries "./vbench/queries/rec_embeds_query.tsv" \
--path-query-filter "./vbench/queries/or_filter.tsv" \
--path-results "./vbench/exact/qrels-multi-dense-no-filter-exact-top50.tsv" \
--start-line 0 \
--end-line 10000

# multi vector + or filter
python get-multi-dense-filter-exact-result.py \
--filter 'or' \
--k 50 \
--log-frequency 100 \
--path-img-embeddings "./vbench/collections/img_embeds_collection.tsv" \
--path-embeds-text "./vbench/collections/rec_embeds_collection.tsv" \
--path-number-data "./vbench/collections/numbers.tsv" \
--path-text-data "./vbench/collections/text.tsv" \
--path-img-queries "./vbench/queries/img_embeds_query.tsv" \
--path-text-queries "./vbench/queries/rec_embeds_query.tsv" \
--path-query-filter "./vbench/queries/or_filter.tsv" \
--path-results "./vbench/exact/qrels-multi-dense-or-filter-exact-top50.tsv" \
--start-line 0 \
--end-line 10000

# multi vector + and filter
python get-multi-dense-filter-exact-result.py \
--filter 'and' \
--k 50 \
--log-frequency 100 \
--path-img-embeddings "./vbench/collections/img_embeds_collection.tsv" \
--path-embeds-text "./vbench/collections/rec_embeds_collection.tsv" \
--path-number-data "./vbench/collections/numbers.tsv" \
--path-text-data "./vbench/collections/text.tsv" \
--path-img-queries "./vbench/queries/img_embeds_query.tsv" \
--path-text-queries "./vbench/queries/rec_embeds_query.tsv" \
--path-query-filter "./vbench/queries/and_filter.tsv" \
--path-results "./vbench/exact/qrels-multi-dense-and-filter-exact-top50.tsv"

# dense + sparse
python get-dense-sparse-exact-result.py \
--filter 'no' \
--path-query "./vbench/queries/text.tsv" \
--path-query-embeds "./vbench/queries/img_embeds_query.tsv" \
--inverted-index-key "text" \
--knn-key "embeds_image" \
--knn-weight 50 --k 50 \
--path-exact-result "./vbench/exact/dense-sparse-top50.tsv"

# dense + sparse + or filter
python get-dense-sparse-exact-result.py \
--filter 'or' \
--path-query-embeds "./vbench/queries/img_embeds_query.tsv" \
--path-query-text "./vbench/queries/text.tsv" \
--path-query-filter "./vbench/queries/or_filter.tsv" \
--inverted-index-key "text" \
--knn-key "embeds_image" \
--knn-weight 50 --k 50 \
--path-exact-result "./vbench/exact/dense-sparse-or-top50.tsv"

# dense + sparse + and filter
python get-dense-sparse-exact-result.py \
--filter 'and' \
--path-query-embeds "./vbench/queries/img_embeds_query.tsv" \
--path-query-text "./vbench/queries/text.tsv" \
--path-query-filter "./vbench/queries/and_filter.tsv" \
--inverted-index-key "text" \
--knn-key "embeds_image" \
--knn-weight 50 --k 50 \
--path-exact-result "./vbench/exact/dense-sparse-and-top50.tsv"
```

### Check Ids
```bash
cd Recipe1M
python3 check-ids.py \
--path-img-embeddings "./vbench/collections/img_embeds_collection.tsv" \
--path-text-embeddings "./vbench/collections/rec_embeds_collection.tsv" \
--path-numbers "./vbench/collections/numbers.tsv" \
--path-text-data "./vbench/collections/text.tsv" \
--path-img-queries "./vbench/queries/img_embeds_query.tsv" \
--path-text-queries "./vbench/queries/rec_embeds_query.tsv" \
--path-query-filter "./vbench/queries/or_filter.tsv" \
--path-query-and-filter "./vbench/queries/and_filter.tsv" \
--path-query-text "./vbench/queries/text.tsv"

python3 check-ids.py \
--path-img-embeddings "./vbench/collections/10k/img_embeds_collection.tsv" \
--path-text-embeddings "./vbench/collections/10k/rec_embeds_collection.tsv" \
--path-numbers "./vbench/collections/10k/numbers.tsv" \
--path-text-data "./vbench/collections/10k/text.tsv" \
--path-img-queries "./vbench/queries/img_embeds_query.tsv" \
--path-text-queries "./vbench/queries/rec_embeds_query.tsv" \
--path-query-filter "./vbench/queries/or_filter.tsv" \
--path-query-and-filter "./vbench/queries/and_filter.tsv" \
--path-query-text "./vbench/queries/text.tsv"
```