def main():
    greeting = input("Greeting: ")
    print("$", value(greeting), sep = "")

def value(greeting):
    grt = greeting.strip().lower()
    if grt.startswith("hello"):
        return 0
    elif grt.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()