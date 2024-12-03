from seasons import time
import pytest

def main():
    test_seasons()

def test_seasons():
    assert time(365) == "Five hundred twenty-five thousand, six hundred minutes"
    assert time(730) == "One million, fifty-one thousand, two hundred minutes"
    assert time(4231) == "Six million, ninety-two thousand, six hundred forty minutes"

if __name__ == "__main__":
    main()
