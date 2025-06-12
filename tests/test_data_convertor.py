from src.data_converter import dataconveter

def test_data_converter_output():
    docs = dataconveter()
    assert isinstance(docs, list)
    assert len(docs) > 0
    assert hasattr(docs[0], 'page_content')
    assert hasattr(docs[0], 'metadata')
