from aganitha import fetcher

def test_extract_email_valid():
    aff = "Department of Biology, Stanford University, CA, USA. Email: example@stanford.edu"
    assert fetcher.extract_email(aff) == "example@stanford.edu"

def test_extract_email_invalid():
    aff = "Department of Physics, MIT"
    assert fetcher.extract_email(aff) == ""

def test_search_pubmed_returns_ids():
    ids = fetcher.search_pubmed("cancer", max_results=3)
    assert isinstance(ids, list)
    assert len(ids) > 0
    assert all(isinstance(i, str) for i in ids)
