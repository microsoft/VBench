echo "Splitting all embedding..."
# `img_embeds_query.tsv`: size 10000
# `rec_embeds_query.tsv`: size 10000
# `img_embeds_collection.tsv`: size 330922
# `rec_embeds_collection.tsv`: size 330922
mkdir -p embedding/split
python split_embedding.py  \
--path-embeddings "im2recipe-Pytorch/results/test" "im2recipe-Pytorch/results/val" "im2recipe-Pytorch/results/train" \
--path-results "embedding/split" \
--queries 10000
