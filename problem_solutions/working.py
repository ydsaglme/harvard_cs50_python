import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    match = re.search(r"^([0-9][0-2]?):?([0-5][0-9])? (AM|PM) to ([0-9][0-2]?):?([0-5][0-9])? (AM|PM)$", s)
    if match:
        start = standardize(int(match.group(1)), match.group(2), match.group(3))
        finish = standardize(int(match.group(4)), match.group(5), match.group(6))
        return f"{start} to {finish}"
    else:
        raise ValueError

def standardize(hour, minute, am_pm):
    if am_pm == "AM":
        if hour == 12:
            hour = 0
    else:
        if hour == 12:
            hour = 12
        else:
            hour += 12
    if minute == None:
        minute = "00"
    return f"{hour:02}:{minute:02}"

if __name__ == "__main__":
    main()
