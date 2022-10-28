echo "Splitting all embedding..."
mkdir -p vbench/collections vbench/queries

python3 split_embedding.py  \
--path-embeddings "im2recipe-Pytorch/results/test" "im2recipe-Pytorch/results/val" "im2recipe-Pytorch/results/train" \
--path-results "vbench" \
--queries 10000
