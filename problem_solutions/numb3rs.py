import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    match = re.search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$", ip)
    if match:
        for i in range(1, 5):
            if int(match.group(i)) > 255 or int(match.group(i)) < 0:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()
