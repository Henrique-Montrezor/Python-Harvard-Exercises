from numb3rs import validate

def test_valid_ips():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("1.2.3.4") == True

def test_out_of_range_ips():
    assert validate("275.3.6.28") == False
    assert validate("1.2.3.999") == False
    assert validate("512.1.1.1") == False
    assert validate("1.512.1.1") == False

def test_invalid_format():
    assert validate("1.2.3") == False
    assert validate("1.2.3.4.5") == False
    assert validate("cat") == False
    assert validate("a.b.c.d") == False
    assert validate("127.0.0") == False
    assert validate("75.456.76.65") == False
    assert validate("127. 0.0.1") == False

def test_first_byte():

    assert validate("1000.1.1.1") == False

def test_string_input():

    assert validate("cat.dog.mouse.rat") == False
