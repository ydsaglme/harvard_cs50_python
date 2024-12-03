import validators

def main():
    print(validate(input("What's your email address? ")))

def validate(s):
    if validators.email(s) == True:
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()
