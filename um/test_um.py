import pytest
from um import count

def test_single_um():
    """Testa a contagem de uma única ocorrência."""
    assert count("um") == 1
    assert count("hello, um, world") == 1

def test_case_insensitivity():
    """Testa se a função ignora maiúsculas/minúsculas."""
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
    assert count("UM, an umbrella") == 1

def test_um_in_words():
    """Testa se 'um' não é contado quando faz parte de outra palavra."""
    assert count("yummy") == 0
    assert count("this is an album") == 0
    assert count("instrument") == 0

def test_no_um():
    """Testa strings que não contêm 'um'."""
    assert count("hello, world") == 0
    assert count("yum") == 0
