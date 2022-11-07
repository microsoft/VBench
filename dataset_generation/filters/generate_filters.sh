cd Recie1M
# Download raw ingredients/instructions
wget http://data.csail.mit.edu/im2recipe/recipe1M_layers.tar.gz -P data
tar -xvf data/recipe1M_layers.tar.gz -C data/ # layer1.json, layer2.json

# Translate vocab.bin to vocab.txt
python3 -m pip install word2vec
python3 im2recipe-Pytorch/scripts/get_vocab.py data/vocab.bin

cd filter_generation
# get ingredients text, number-ingredients, number-instructions from lmdb
python3 -m pip install lmdb
python3 keywords.py --partition 'collection' --path-result-keywords "../data/collections/keywords.tsv" --path-result-numbers "../data/collections/numbers.tsv"
python3 keywords.py --partition 'query' --path-result-keywords "../data/queries/keywords.tsv" --path-result-keywords "../data/queries/numbers.tsv"

# get ingredients and instructions text of collection
python3 text.py --path-result '../data/collections/text.tsv' --partition 'collection' --json '../data/layer1.json'
# get ingredients and instructions text of query
python3 text.py --path-result '../data/queries/text.tsv' --partition 'query' --json '../data/layer1.json'

# generate scalar filters
python3 or_filter_query.py
python3 and_filter_query.py

# check ids
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
