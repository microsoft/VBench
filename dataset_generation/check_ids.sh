# check ids
python3 check_ids.py \
--path-img-embeddings "./vbench/collections/img_embeds.tsv" \
--path-text-embeddings "./vbench/collections/rec_embeds.tsv" \
--path-numbers "./vbench/collections/numbers.tsv" \
--path-text-data "./vbench/collections/text.tsv" \
--path-img-queries "./vbench/queries/img_embeds.tsv" \
--path-text-queries "./vbench/queries/rec_embeds.tsv" \
--path-query-filter "./vbench/queries/or_filter.tsv" \
--path-query-and-filter "./vbench/queries/and_filter.tsv" \
--path-query-text "./vbench/queries/text.tsv"

python3 check_ids.py \
--path-img-embeddings "./vbench/collections/10k/img_embeds.tsv" \
--path-text-embeddings "./vbench/collections/10k/rec_embeds.tsv" \
--path-numbers "./vbench/collections/10k/numbers.tsv" \
--path-text-data "./vbench/collections/10k/text.tsv" \
--path-img-queries "./vbench/queries/img_embeds.tsv" \
--path-text-queries "./vbench/queries/rec_embeds.tsv" \
--path-query-filter "./vbench/queries/or_filter.tsv" \
--path-query-and-filter "./vbench/queries/and_filter.tsv" \
--path-query-text "./vbench/queries/text.tsv"