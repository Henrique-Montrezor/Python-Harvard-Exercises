# test_twttr.py

from twttr import shorten

def test_shorten_lowercase():
    assert shorten("twitter") == "twttr"
    assert shorten("hello, world") == "hll, wrld"

def test_shorten_uppercase():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("HELLO, WORLD") == "HLL, WRLD"
    assert shorten("CS50") == "CS50"

def test_shorten_mixed_case():
    assert shorten("What's your name?") == "Wht's yr nm?"

def test_shorten_numbers():
    assert shorten("CS50P") == "CS50P"
    assert shorten("12345") == "12345"

def test_shorten_punctuation():
    assert shorten("!@#$%^") == "!@#$%^"
    assert shorten("h.e,l:l;o") == "h.,l:l;"
