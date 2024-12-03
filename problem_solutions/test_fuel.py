from fuel import convert, gauge
import pytest

def main():
    test_convert()
    test_gauge()

def test_convert():
    assert convert("1/100") == 1
    assert convert("50/100") == 50
    assert convert("99/100") == 99
    with pytest.raises(ValueError):
        convert("101/100")
    with pytest.raises(ZeroDivisionError):
        convert("50/0")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"

if __name__ == "__main__":
    main()