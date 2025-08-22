import pytest
from src.utils import validate_email, sanitize_string, calculate_percentage

def test_validate_email():
    assert validate_email('test@example.com') == True
    assert validate_email('user.name@domain.co.uk') == True
    assert validate_email('invalid.email') == False
    assert validate_email('@example.com') == False
    assert validate_email('test@') == False

def test_sanitize_string():
    assert sanitize_string('Hello@World!') == 'HelloWorld'
    assert sanitize_string('Test#123$') == 'Test123'
    assert sanitize_string('  spaces  ') == 'spaces'

def test_calculate_percentage():
    assert calculate_percentage(25, 100) == 25.0
    assert calculate_percentage(33, 100) == 33.0
    assert calculate_percentage(1, 3) == 33.33
    assert calculate_percentage(5, 0) is None