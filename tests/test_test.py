# tests/test_app.py
def test_basic():
    assert 1 + 1 == 2

def test_import():
    from src.app import app
    assert app is not None