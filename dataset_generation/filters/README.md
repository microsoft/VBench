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


## Filters Generation

```bash
bash ./generate_filters.sh
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
