from app import add, subtract

def test_add():
    assert add(2, 3) == 5  # This will FAIL because add returns 6
    

def test_subtract():
    assert subtract(5, 2) == 3  # This will PASS
