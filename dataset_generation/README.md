## Get Recipe1M Dataset Embeddings

Run `get_embedding.sh`, the results will be saved in `im2recipe-Pytorch/results`

## Split embeddings to generate the vector fileds

Run `split_embedding.sh`, the following files will be generated:

- `vbench/queries/img_embeds.tsv`: size 10000
- `vbench/queries/rec_embeds.tsv`: size 10000
- `vbench/collections/img_embeds.tsv`: size 330922
- `vbench/collections/rec_embeds.tsv`: size 330922

## Generate Filters

Run `filters/generate_filters.sh`.

## Sanity Check

Run `check_ids.sh` to make sure that the ids in different files are aligned.

## Get Sub collection

Run `python get_sub_collection.py --size-subcollection 10000 --path-result "vbench/collections/10k"`.
