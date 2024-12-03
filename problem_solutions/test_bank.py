from bank import value

def main():
    test_bank()

def test_bank():
    assert value("Hello") == 0
    assert value("Hey") == 20
    assert value("Good morning") == 100

if __name__ == "__main__":
    main()