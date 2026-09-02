from client import HierarchicalHnswVectorIndexAnnSearcherClient

def main():
    client = HierarchicalHnswVectorIndexAnnSearcherClient()
    res = client.query_ann_neighbors(768, 8, 48)
    print('HNSW Vector ANN Searcher: ' + res['search_operation_id'] + ' (Index Size: ' + str(res['index_vectors_count']) + ' vectors)')
    print('Neighbors: ' + str(res['nearest_neighbors_returned_count']) + ' | Query Latency: ' + str(res['query_latency_micros']) + 'us | Recall: ' + str(res['recall_rate_estimate_pct']) + '%')
    print('Index Manifest: ' + res['vector_index_manifest_url'])

if __name__ == '__main__':
    main()
