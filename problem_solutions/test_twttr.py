from twttr import shorten

def main():
    test_twttr()

def test_twttr():
    assert shorten("liverpool") == "lvrpl"
    assert shorten("LIVERPOOL") == "LVRPL"
    assert shorten("LiverpooL") == "LvrpL"
    assert shorten("1892") == "1892"
    assert shorten("'!") == "'!"

if __name__ == "__main__":
    main()
