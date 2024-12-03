import sys
import csv
import tabulate

try:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-3] != "c":
            sys.exit("Not a CSV file")
        else:
            with open(sys.argv[1]) as pizza_table:
                reader = csv.DictReader(pizza_table)
                print(tabulate.tabulate(reader, headers = "keys", tablefmt = "grid"))

except FileNotFoundError:
    sys.exit("File does not exist")
