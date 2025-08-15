# test_plates.py

from plates import is_valid

def test_length():
    assert is_valid("AA") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False

def test_start_with_two_letters():
    assert is_valid("CS") == True
    assert is_valid("50") == False
    assert is_valid("C5") == False
    assert is_valid("5C") == False

def test_numbers_placement():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("CS50P2") == False

def test_first_number_not_zero():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

def test_punctuation():
    assert is_valid("PI3.14") == False
    assert is_valid("CS 50") == False
    assert is_valid("CS,50") == False

def test_valid_cases():
    assert is_valid("ECTO88") == True
    assert is_valid("NRVOUS") == True
