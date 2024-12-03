def main():
    fraction = input("Fraction: ")
    print(gauge(convert(fraction)))

def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            percentage = (x / y) * 100
            if int(x) > int(y):
                raise ValueError
            elif int(y) == 0:
                raise ZeroDivisionError
            else:
                return percentage
        except:
            pass

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        rounded_percentage = str(round(percentage)) + "%"
        return rounded_percentage

if __name__ == "__main__":
    main()