from aganitha import filter

def test_is_non_academic_true():
    aff = "XYZ Biotech Inc., California"
    assert filter.is_non_academic(aff) is True

def test_is_non_academic_false():
    aff = "Department of Physics, Stanford University"
    assert filter.is_non_academic(aff) is False

def test_find_corresponding_email_found():
    authors = [
        {"name": "John", "email": ""},
        {"name": "Jane", "email": "jane@example.com"},
    ]
    assert filter.find_corresponding_email(authors) == "jane@example.com"

def test_find_corresponding_email_not_found():
    authors = [
        {"name": "John", "email": ""},
        {"name": "Jane", "email": ""},
    ]
    assert filter.find_corresponding_email(authors) == ""
