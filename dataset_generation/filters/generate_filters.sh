cd Recie1M
# Download raw ingredients/instructions
wget http://data.csail.mit.edu/im2recipe/recipe1M_layers.tar.gz -P data
tar -xvf data/recipe1M_layers.tar.gz -C data/ # layer1.json, layer2.json

# Translate vocab.bin to vocab.txt
python3 -m pip install word2vec
python3 im2recipe-Pytorch/scripts/get_vocab.py data/vocab.bin

cd filters
# get ingredients text, number-ingredients, number-instructions from lmdb
python3 -m pip install lmdb
python3 get_keywords.py --partition 'collection' --path-result-keywords "../vbench/collections/keywords.tsv" --path-result-numbers "../vbench/collections/numbers.tsv"
python3 get_keywords.py --partition 'query' --path-result-keywords "../vbench/queries/keywords.tsv" --path-result-numbers "../vbench/queries/numbers.tsv"

# get ingredients and instructions text
python3 get_text.py --path-result '../vbench/collections/text.tsv' --partition 'collection' --json '../data/layer1.json'
python3 get_text.py --path-result '../vbench/queries/text.tsv' --partition 'query' --json '../data/layer1.json'

# get price
python3 generate_price.py --path-result '../vbench/collections/price.tsv' --partition 'collection'
python3 generate_price.py --path-result '../vbench/queries/price.tsv' --partition 'query'

# generate scalar filters
# python3 generate_numeric_filters.py
python3 generate_string_filters.py
