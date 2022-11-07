## Ground Truth Calculation

Exact results can be calculated in a brute-force manner with the following scripts: 

```bash
bash exact_result/get_exact_result.sh
bash exact_result/get_exact_result_10k.sh
```

## Evaluation

For Search results in [recommended format](evaluation/examples), you can get recall/latency with the following scripts:

```bash
# recall
python evaluation/calculate-recall.py \
    --path-search-results "path-to-your-search-result" \
    --path-exact-results "path-to-ground-truth"
# latency
python evaluation/calculate-latency.py \
    --path-latency-result "path-to-your-latency-result"
```