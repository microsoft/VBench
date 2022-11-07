--Q1:Single-Vector TopK
SELECT recipe_id,
    COSINE_DISTANCE(images_embedding, p_images_embedding) AS d
FROM Recipe
ORDER BY d
LIMIT K;

--Q2:Multi-Vector (Dense) TopK
SELECT recipe_id,
    COSINE_DISTANCE(images_embedding, p_images_embedding) AS d1,
    COSINE_DISTANCE(description_embedding, p_description_embedding) AS d2
FROM Recipe
ORDER BY d1 * WEIGHT + d2
LIMIT K;

--Q3:Multi-Vector (Dense + Sparse) TopK
SELECT recipe_id,
    COSINE_DISTANCE(description_embedding, p_description_embedding) AS d1,
    BM25_DISTANCE(description, p_description) AS d2
FROM Recipe
ORDER BY d1 * WEIGHT + d2 
LIMIT K;

--Q4:Single-Vector TopK + Numeric Filter
SELECT recipe_id,
    COSINE_DISTANCE(images_embedding, p_images_embedding) AS d,
FROM Recipe
WHERE  (p_num_ingredients <= num_ingredients)
  OR (p_num_instructions <= num_instructions)
ORDER BY d
LIMIT K;

--Q5:Multi-Vector (Dense) TopK + Numeric Filter
SELECT recipe_id,
    COSINE_DISTANCE(images_embedding, p_images_embedding) AS d1,
    COSINE_DISTANCE(description_embedding, p_description_embedding) AS d2
FROM Recipe
WHERE  (p_num_ingredients <= num_ingredients)
  OR (p_num_instructions <= num_instructions)
ORDER BY d1 * WEIGHT + d2
LIMIT K;

--Q6:Multi-Vector (Dense + Sparse) TopK + Numeric Filter
SELECT recipe_id,
    COSINE_DISTANCE(description_embedding, p_description_embedding) AS d1,
    BM25_DISTANCE(description, p_description) AS d2
FROM Recipe
WHERE  (p_num_ingredients <= num_ingredients)
  OR (p_num_instructions <= num_instructions)
ORDER BY d1 * WEIGHT + d2 
LIMIT K;

--Q7:Single-Vector TopK + String Filter
SELECT recipe_id,
    COSINE_DISTANCE(images_embedding, p_images_embedding) AS d,
FROM Recipe
WHERE (ingredients LIKE "%p_ingredients_1%")
 AND (ingredients NOT LIKE "%p_ingredients_2%")
ORDER BY d
LIMIT K;

--Q8:Multi-Vector (Dense) TopK + String Filter
SELECT recipe_id,
    COSINE_DISTANCE(images_embedding, p_images_embedding) AS d1,
    COSINE_DISTANCE(description_embedding, p_description_embedding) AS d2
FROM Recipe
WHERE (ingredients LIKE "%p_ingredients_1%")
 AND (ingredients NOT LIKE "%p_ingredients_2%")
ORDER BY d1 * WEIGHT + d2
LIMIT K;

--Q9:Multi-Vector (Dense+Sparse) TopK + String Filter
SELECT recipe_id,
    COSINE_DISTANCE(description_embedding, p_description_embedding) AS d1,
    BM25_DISTANCE(description, p_description) AS d2
FROM Recipe
WHERE (ingredients LIKE "%p_ingredients_1%")
 AND (ingredients NOT LIKE "%p_ingredients_2%")
ORDER BY d1 * WEIGHT + d2 
LIMIT K;

--Q10:Single-Vector Search + Vector Filtering
SELECT recipe_id,
    COSINE_DISTANCE(images_embedding, p_images_embedding) AS d
FROM Recipe
WHERE d <= D

--Q11:Join
SELECT Recipe.recipe_id, Tag.tag_name
FROM Recipe JOIN Tag
ON COSINE_DISTANCE(Recipe.images_embedding, 
        Tag.tag_vector) <= D;

--Q12:Group By
SET GROUP_BY_DISTANCE_THRESHOLD = D
SELECT ARRAY_AGG(recipe_id)
FROM Recipe
GROUP BY images_embedding
