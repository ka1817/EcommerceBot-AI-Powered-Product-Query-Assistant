from src.query_rewritting import query_rewriting

def test_query_rewriting():
    query = "cheap laptop with good battery"
    rewritten = query_rewriting(query)
    assert isinstance(rewritten, str)
    assert rewritten != ""
    assert rewritten != query
