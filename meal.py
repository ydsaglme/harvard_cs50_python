def main():
    time = input("What time is it? ")
    if 7 <= convert(time) <= 8:
        print("breakfast time")
    elif 12 <= convert(time) <= 13:
        print("lunch time")
    elif 18 <= convert(time) <= 19:
        print("dinner time")
    else:
        return

def convert(time):
    hours, minutes = time.strip().split(":")
    h = float(hours)
    m = float(minutes) / 60
    n = h + m
    return float(n)

if __name__ == "__main__":
    main()
