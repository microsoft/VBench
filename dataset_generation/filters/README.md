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
python get_filter_selectivity.py \
--path-numbers '../vbench/collections/numbers.tsv' \
--path-text "../vbench/collections/text.tsv" \
--path-or-filter "../vbench/queries/or_filter.tsv" \
--path-and-filter "../vbench/queries/and_filter.tsv" \
--path-img-embeddings "../vbench/collections/img_embeds.tsv" \
--path-img-queries "../vbench/queries/img_embeds.tsv"
```
