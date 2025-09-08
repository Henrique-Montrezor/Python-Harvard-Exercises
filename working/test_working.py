import pytest
from working import convert

def test_valid_formats():
    """Testa conversões válidas, incluindo os exemplos do problema."""
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test_edge_cases():
    """Testa casos limite como meio-dia e meia-noite."""
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"

def test_invalid_hour():
    """Testa se um ValueError é levantado para horas inválidas (ex: 13 PM)."""
    with pytest.raises(ValueError):
        convert("13 PM to 5 PM")
    with pytest.raises(ValueError):
        convert("9 AM to 14 PM")

def test_invalid_minute():
    """Testa se um ValueError é levantado para minutos inválidos (ex: :60)."""
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:70 PM")

def test_missing_to():
    """Testa se um ValueError é levantado se faltar o 'to'."""
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("9AM to 5PM") # Falta o espaço antes de AM/PM

def test_invalid_overall_format():
    """Testa outros formatos completamente inválidos."""
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("9:00 to 17:00") # Formato de 24h não é aceito como entrada
