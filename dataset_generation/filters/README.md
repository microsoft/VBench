## Dataset
| collection/query | file                         | columns                                         | notes                                  |
| ---------------- | ---------------------------- | ----------------------------------------------- | -------------------------------------- |
| collection       | `collections/text.tsv`       | 'id','ingredients','instructions'               | ingredients/instructions text          |
| collection       | `collection/keywords.tsv`    | 'id','ingredients'                              | ingredients keywords                   |
| collection       | `collection/numbers.tsv`     | 'id','number-ingredients','number-instructions' | number of ingredients and instructions |
| query            | `queries/text.tsv`           | 'id','ingredients','instructions'               | ingredients/instructions text          |
| query            | `queries/numeric_filter.tsv` | 'id','num-instructions'                         | numeric filter                         |
| query            | `queries/string_filter.tsv`  | 'id','ingredientword'                           | string filter                          |


## Filters Generation

```bash
bash ./generate_filters.sh
```

## Filter Analysis
Get the selectivity distribution of the filters:

```bash
python3 get_filter_selectivity.py \
--path-numbers '../vbench/collections/price.tsv' \
--path-text "../vbench/collections/text.tsv" \
--path-numeric-filter "../vbench/queries/price.tsv" \
--path-string-filter "../vbench/queries/string_filter.tsv" \
--path-img-embeddings "../vbench/collections/img_embeds.tsv" \
--path-img-queries "../vbench/queries/img_embeds.tsv"
```
