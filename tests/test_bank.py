# test_bank.py

from bank import value

def test_value_hello():
    assert value("hello") == 0
    assert value("Hello, Newman") == 0
    assert value("  HELLO   ") == 0

def test_value_h():
    assert value("How you doing?") == 20
    assert value("hey") == 20
    assert value("  howdy  ") == 20

def test_value_other():
    assert value("What's happening?") == 100
    assert value("good morning") == 100
    assert value("Yo") == 100

def test_value_case_insensitivity():
    assert value("HELLO") == 0
    assert value("HOLA") == 20
    assert value("WHAT'S UP?") == 100
