from src.ingest import ingestdata

def test_vector_store_creation():
    vector_store = ingestdata()
    assert vector_store is not None
    assert hasattr(vector_store, 'as_retriever')
