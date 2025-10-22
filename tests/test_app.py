from dedupe import dedupe_header
def test_unique_columns():
 assert dedupe_header(["id", "name", "age"]) == ["id", "name", "age"]
def test_duplicate_columns():
 assert dedupe_header(["id", "id", "id"]) == ["id", "id.1", "id.2"]
def test_mixed_columns():
 cols = ["id", "name", "id", "name", "name"]
 expected = ["id", "name", "id.1", "name.1", "name.2"]
 assert dedupe_header(cols) == expected
