# test_fuel.py

import pytest
from fuel import convert, gauge

def test_convert_valid_fraction():
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("3/4") == 75

def test_convert_value_error():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("1.5/3")
    with pytest.raises(ValueError):
        convert("2/1")
    with pytest.raises(ValueError):
        convert("-1/4") 

def test_convert_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge_output():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
