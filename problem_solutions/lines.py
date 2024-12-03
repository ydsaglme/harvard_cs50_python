import sys

try:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-2] != "p":
            sys.exit("Not a Python file")
        else:
            count = 0
            with open(sys.argv[1]) as file:
                for line in file:
                    if not (line.lstrip().startswith("#") or line.strip() == ""):
                        count += 1
                print(count)

except FileNotFoundError:
    sys.exit("File does not exist")