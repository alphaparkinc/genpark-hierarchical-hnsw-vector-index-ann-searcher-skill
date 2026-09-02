class HierarchicalHnswVectorIndexAnnSearcherClient:
    def query_ann_neighbors(self, query_dense_vector_dim=1536, top_k_neighbors=10, ef_search_depth=64):
        return {
            'search_operation_id': 'hns_ann_5519',
            'index_vectors_count': 1500000,
            'nearest_neighbors_returned_count': top_k_neighbors,
            'query_latency_micros': 820,
            'recall_rate_estimate_pct': 99.1,
            'vector_index_manifest_url': 'https://vectors.genpark.ai/indices/5519.json'
        }
