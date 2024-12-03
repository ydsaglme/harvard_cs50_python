def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not s[:2].isalpha():
        return False
    if 6 < len(s) or len(s) < 2:
        return False
    i = 0
    while i < len(s):
        if s[i].isnumeric() == True:
            if not s[i:].isnumeric():
                return False
            elif s[i] == "0":
                return False
            else:
                return True
        i = i + 1
    for character in s:
        if not character.isalnum():
            return False
    return True

if __name__ == "__main__":
    main()
