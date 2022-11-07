VBench is a benchmark for evaluating vector analytic-queries based on SQL interface.
VBench uses Recipe1M dataset augmented with scalar attributes, and provides a comprehensive set of vector analytic-queries that utilize standard SQL operators, including Join, GroupBy, Filter and TopK.

In this repo, we provides instructions on 
- how to cook the VBench dataset
- how to evaluate the vector-analytic engines on it

## VBench Dataset

VBench dataset consists of two tables: Recipe Table and Tag Table.

- Recipe Table

| Column Name           | Data Type      | Example                       | Notes                         |
| --------------------- | -------------- | ----------------------------- | ----------------------------- |
| recipe_id             | Identifier     | 1                             | primary key                   |
| images                | list of String | ['data/images/1/0.jpg', ...]  | paths of images               |
| description           | Text           | [ingredients] + [instruction] | sparse vector                 |
| images_embedding      | Vector         | [-0.0421, 0.0296, ...,0.0273] | dense vector, 1024 dimensions |
| description_embedding | Vector         | [0.0056,-0.0487,..., 0.0034]  | dense vect, 1024 dimensions   |
| num_ingredients       | Integer        | 3                             | number of ingredients         |
| num_instructions      | Integer        | 5                             | number of instruction steps   |


- Tag Table

| Column Name | Data Type  | Example                      | Notes                                       |
| ----------- | ---------- | ---------------------------- | ------------------------------------------- |
| id          | Identifier | 1                            | primary key                                 |
| tag_name    | Text       | "salad"                      | name of the tag                             |
| tag_vector  | Vector     | [-0.0137, 0.0421,...,0.0183] | embedding or weight vector, 1024 dimensions |


Please refer to `dataset_generation/README.md` for detail insructions on how to generate these two tables.


## VBench Queries

VBench has `12` queries, which can be divided into four categories: 
- Top-K 
- Vector filtering
- Join
- Group By
The queries utilize standard SQL operators over vector and scalar columns 
Please refer to `quereis.sql` for detail.

## Evaluation

Please refer to `evaluation/README.md` for detail insructions on how to evaluate different vector search engines.

## License
The entire codebase is under [MIT license](./LICENSE).
