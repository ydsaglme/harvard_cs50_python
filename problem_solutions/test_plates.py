from plates import is_valid

def main():
    test_plates()

def test_plates():
    assert is_valid("H") == False
    assert is_valid("50") == False
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("PI3.14") == False
    assert is_valid("OUTATIME") == False

if __name__ == "__main__":
    main()
