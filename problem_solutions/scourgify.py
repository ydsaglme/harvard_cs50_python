import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    try:
        students = []
        with open(sys.argv[1], "r") as r_file, open(sys.argv[2], "w") as w_file:
            reader = csv.DictReader(r_file)
            for line in reader:
                l_name, f_name = line["name"].split(",")
                house = line["house"]
                students.append({"first": f_name.lstrip(), "last": l_name, "house": house})
            writer = csv.DictWriter(w_file, fieldnames = ["first", "last", "house"])
            writer.writeheader()
            for line in students:
                writer.writerow({"first": line["first"], "last": line["last"], "house": line["house"]})

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
