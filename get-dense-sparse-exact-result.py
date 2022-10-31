# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
import csv
import json
import argparse
import requests

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)


def search_query_dense_sparse(inverted_index_key, knn_key, knn_weight, query, query_embeds, k):
    """return a tuple(docid, rank, score)
    """
    url = "https://localhost:9200/recipe/_search"
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        "size": k,
        "query": {
            "bool": {
                "should": [
                    {
                        "script_score": {
                            "query": {
                                "match_all": {}
                            },
                            "script": {
                                "source": "knn_score",
                                "lang": "knn",
                                "params": {
                                    "field": knn_key,
                                    "query_value": query_embeds,
                                    "space_type": "cosinesimil"
                                }
                            }
                        }
                    },
                    {
                        "script_score": {
                            "query": {
                                "match": {
                                    inverted_index_key: query
                                }
                            },
                            "script": {
                                "source": "_score / " + str(knn_weight)
                            }
                        }
                    }
                ],
                "minimum_should_match": 2
            }
        }
    }
    response = requests.request("GET", url, headers=headers, data=json.dumps(payload), verify=False, auth=('admin', 'admin'))
    res = json.loads(response.text)
    return [(record["_source"]["itemid"], idx+1, record["_score"]) for idx, record in enumerate(res["hits"]["hits"])]


def search_query_dense_sparse_or_filter(inverted_index_key, knn_key, knn_weight, query, query_embeds, filter1, filter2, k):
    """return a tuple(docid, rank, score)
    """
    url = "https://localhost:9200/recipe/_search"
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        "size": k,
        "query": {
            "bool": {
                "should": [
                    {
                        "script_score": {
                            "query": {
                                "match_all": {}
                            },
                            "script": {
                                "source": "knn_score",
                                "lang": "knn",
                                "params": {
                                    "field": knn_key,
                                    "query_value": query_embeds,
                                    "space_type": "cosinesimil"
                                }
                            }
                        }
                    },
                    {
                        "script_score": {
                            "query": {
                                "match": {
                                    inverted_index_key: query
                                }
                            },
                            "script": {
                                "source": "_score / " + str(knn_weight)
                            }
                        }
                    }
                ],
                "minimum_should_match": 2,
                "filter": [{
                    "bool": {
                        "should": [
                            {"range": {"number_ingredients": {"lte": filter1}}},
                            {"range": {"number_instructions": {"lte": filter2}}}
                        ]
                    }
                }]
            }
        }
    }
    response = requests.request("GET", url, headers=headers, data=json.dumps(payload), verify=False, auth=('admin', 'admin'))
    res = json.loads(response.text)
    return [(record["_source"]["itemid"], idx+1, record["_score"]) for idx, record in enumerate(res["hits"]["hits"])]


def search_query_dense_sparse_and_filter(inverted_index_key, knn_key, knn_weight, query, query_embeds, filter1, filter2, k):
    """return a tuple(docid, rank, score)
    """
    url = "https://localhost:9200/recipe/_search"
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        "size": k,
        "query": {
            "bool": {
                "should": [
                    {
                        "script_score": {
                            "query": {
                                "match_all": {}
                            },
                            "script": {
                                "source": "knn_score",
                                "lang": "knn",
                                "params": {
                                    "field": knn_key,
                                    "query_value": query_embeds,
                                    "space_type": "cosinesimil"
                                }
                            }
                        }
                    },
                    {
                        "script_score": {
                            "query": {
                                "match": {
                                    inverted_index_key: query
                                }
                            },
                            "script": {
                                "source": "_score / " + str(knn_weight)
                            }
                        }
                    }
                ],
                "minimum_should_match": 2,
                "filter": {
                    "match": {"text": filter1.replace('_', ' ')}
                },
                "must_not": {
                    "match": {"text": filter2.replace('_', ' ')}
                }
            }
        }
    }
    response = requests.request("GET", url, headers=headers, data=json.dumps(payload), verify=False, auth=('admin', 'admin'))
    res = json.loads(response.text)
    return [(record["_source"]["itemid"], idx+1, record["_score"]) for idx, record in enumerate(res["hits"]["hits"])]


def search_queries_dense_sparse(path_query_text, inverted_index_key, path_query_embeds, knn_key, knn_weight, path_qrels, k, queries=-1, print_frequency=100):
    with open(path_query_text, 'rt', encoding="utf8") as f_query_text, \
            open(path_query_embeds, 'rt', encoding="utf8") as f_query_embeds, \
            open(path_qrels, 'w', encoding="utf8") as out:
        tsvreader_text = csv.reader(f_query_text, delimiter="\t")
        tsvreader_embeds = csv.reader(f_query_embeds, delimiter="\t")
        idx = 0
        for [qid, ingredients, instructions], [_, query_embeds] in zip(tsvreader_text, tsvreader_embeds):
            # text = ingredient.replace('_', ' ') + " " + instruction.replace('_', ' ')
            query_text = ingredients + instructions
            query_embeds = [float(ele) for ele in query_embeds[1:-1].split(', ')]
            result = search_query_dense_sparse(inverted_index_key, knn_key, knn_weight, query_text, query_embeds, k)
            for (rid, rank, score) in result:
                out.write(f"{qid}\t{rid}\t{rank}\t{score}\n")

            idx += 1
            if idx % print_frequency == 0:
                out.flush()
                print(f"{idx} queries searched...")
            if queries != -1 and idx >= queries:
                break
        print(f"{idx} queries searched.")


def search_queries_dense_sparse_filter(path_query_text, inverted_index_key, path_query_embeds, knn_key, filter, path_query_filter, knn_weight, path_qrels, k, queries=-1, print_frequency=100):
    with open(path_query_text, 'rt', encoding="utf8") as f_query_text, \
            open(path_query_filter, 'rt', encoding="utf8") as f_filter, \
            open(path_query_embeds, 'rt', encoding="utf8") as f_query_embeds, \
            open(path_qrels, 'w', encoding="utf8") as out:
        tsvreader_text = csv.reader(f_query_text, delimiter="\t")
        tsvreader_filter = csv.reader(f_filter, delimiter="\t")
        tsvreader_embeds = csv.reader(f_query_embeds, delimiter="\t")
        idx = 0
        for [qid, ingredients, instructions], [_, query_embeds], [_, filter1, filter2] in zip(tsvreader_text, tsvreader_embeds, tsvreader_filter):
            # text = ingredient.replace('_', ' ') + " " + instruction.replace('_', ' ')
            query_text = ingredients + instructions
            query_embeds = [float(ele) for ele in query_embeds[1:-1].split(', ')]
            if filter == 'or':
                filter1 = int(filter1)
                filter2 = int(filter2)
                result = search_query_dense_sparse_or_filter(
                    inverted_index_key, knn_key, knn_weight, query_text, query_embeds, filter1, filter2, k)
            else:
                result = search_query_dense_sparse_and_filter(
                    inverted_index_key, knn_key, knn_weight, query_text, query_embeds, filter1, filter2, k)

            for (rid, rank, score) in result:
                out.write(f"{qid}\t{rid}\t{rank}\t{score}\n")

            idx += 1
            if idx % print_frequency == 0:
                out.flush()
                print(f"{idx} queries searched...")
            if queries != -1 and idx >= queries:
                break
        print(f"{idx} queries searched.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--filter', type=str, default='no',
                        help='no, or, and')
    parser.add_argument('--path-query-filter', type=str, default="./data/vbench/queries/or_filter.tsv",
                        help='path to queries filter')
    parser.add_argument('--path-query-text', type=str, default='./data/vbench/queries/text.tsv',
                        help='path to query')
    parser.add_argument('--path-query-embeds', type=str,
                        default='./data/vbench/queries/img_embeds_query.tsv',
                        help='path to query embedding result')
    parser.add_argument('--inverted-index-key', type=str, default='text',
                        help='text')
    parser.add_argument('--knn-key', type=str, default='embeds_image',
                        help='embeds_image')
    parser.add_argument('--knn-weight', type=int, default=50,
                        help='wight of knn in combine search')
    parser.add_argument('--k', type=int, default=50,
                        help='the number of knn to return')
    parser.add_argument('--path-exact-result', type=str, default="../result/exact/qrels-dense-sparse-exact-top50.tsv",
                        help='path to save search result')
    parser.add_argument('--queries-to-search', type=int, default=-1,
                        help='number of queries to search')
    parser.add_argument('--log-frequency', type=int, default=100,
                        help='log frequency')

    args = parser.parse_args()

    if args.filter == 'no':
        search_queries_dense_sparse(
            args.path_query_text, args.inverted_index_key,
            args.path_query_embeds, args.knn_key,
            args.knn_weight, args.path_exact_result,
            args.k, args.queries_to_search, args.log_frequency)
    else:
        search_queries_dense_sparse_filter(
            args.path_query_text, args.inverted_index_key,
            args.path_query_embeds, args.knn_key,
            args.filter, args.path_query_filter,
            args.knn_weight, args.path_exact_result,
            args.k, args.queries_to_search, args.log_frequency)
