## Dataset
| collection/query | file                      | columns                                        | notes                                  |
| ---------------- | ------------------------- | ---------------------------------------------- | -------------------------------------- |
| collection       | `collections/text.tsv`    | 'id','ingredients','instructions'              | ingredients/instructions text          |
| collection       | `collection/keywords.tsv` | 'id','ingredients'                             | ingredients keywords                   |
| collection       | `collection/numbers.tsv`  | 'id','number-ingredients','number-collections' | number of ingredients and instructions |
| query            | `queries/text.tsv`        | 'id','ingredients','instructions'              | ingredients/instructions text          |
| query            | `queries/keywords.tsv`    | 'id','ingredients'                             | ingredients keywords                   |
| query            | `queries/numbers.tsv`     | 'id','number-ingredients','number-collections' | number of ingredients and instructions |
| query            | `queries/or_filter.tsv`   | 'id','num_ingredients                          | `or` filter                            |
| query            | `queries/and_filter.tsv`  | 'id','ingredientword-0','ingredientword-1'     | `and` filter                           |

## Scripts
```bash
cd Recie1M
# Download raw ingredients/instructions
wget http://data.csail.mit.edu/im2recipe/recipe1M_layers.tar.gz -P data
tar -xvf data/recipe1M_layers.tar.gz -C data/ # layer1.json, layer2.json

# Download lmdb source file and vocab source file, which may have been downloaded before in ./Recipe1M/get-embedding.sh
wget http://data.csail.mit.edu/im2recipe/train.tar -P data
wget http://data.csail.mit.edu/im2recipe/val.tar -P data
wget http://data.csail.mit.edu/im2recipe/test.tar -P data
wget http://data.csail.mit.edu/im2recipe/recipe1M_pretrained/vocab.bin.gz -P data
gzip -d data/vocab.bin.gz
mkdir data/train
tar -xvf data/train.tar -C data/train/
mkdir data/val
tar -xvf data/val.tar -C data/val/
mkdir data/test
tar -xvf data/test.tar -C data/test/

# Translate vocab.bin to vocab.txt
python3 -m pip install word2vec
python3 im2recipe-Pytorch/scripts/get_vocab.py data/vocab.bin

cd data_gen
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
```

## Filter Analysis
Get the selectivity distribution of the filters:

```bash
python get-filter-selectivity.py \
--path-numbers '../VBench/Recipe1M/vbench/collections/numbers.tsv' \
--path-text "../VBench/Recipe1M/vbench/collections/text.tsv" \
--path-or-filter "../VBench/Recipe1M/vbench/queries/or_filter.tsv" \
--path-and-filter "../VBench/Recipe1M/vbench/queries/and_filter.tsv" \
--path-img-embeddings "../VBench/Recipe1M/vbench/collections/img_embeds_collection.tsv" \
--path-img-queries "../VBench/Recipe1M/vbench/queries/img_embeds_query.tsv"
```
