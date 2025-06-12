from src.retrival_genaration import generation
from src.ingest import ingestdata

def test_generation_pipeline():
    vstore = ingestdata()
    chain = generation(vstore)
    assert chain is not None
