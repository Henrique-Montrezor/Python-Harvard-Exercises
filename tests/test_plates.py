# test_plates.py

from plates import is_valid

# Teste para a Regra 1: Comprimento da placa (min 2, max 6)
def test_length():
    """Testa o comprimento da placa."""
    assert is_valid("AA") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False

# Teste para a Regra 2: Placa deve começar com duas letras
def test_start_with_two_letters():
    """Testa se a placa começa com duas letras."""
    assert is_valid("CS") == True
    assert is_valid("50") == False
    assert is_valid("C5") == False
    assert is_valid("5C") == False

# Teste para a Regra 3: Números devem vir no final, não no meio
def test_numbers_placement():
    """Testa se os números estão apenas no final."""
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("CS50P2") == False

# Teste para a Regra 4: O primeiro número usado não pode ser '0'
def test_first_number_not_zero():
    """Testa se o primeiro número não é '0'."""
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

# Teste para a Regra 5: Sem pontuação, espaços ou caracteres especiais
def test_punctuation():
    """Testa a ausência de pontuação."""
    assert is_valid("PI3.14") == False
    assert is_valid("CS 50") == False
    assert is_valid("CS,50") == False

# Teste geral com placas válidas conhecidas
def test_valid_cases():
    """Testa placas que devem ser consideradas válidas."""
    assert is_valid("ECTO88") == True
    assert is_valid("NRVOUS") == True
