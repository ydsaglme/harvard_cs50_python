from datetime import date
import inflect
import sys

p = inflect.engine()

def main():
    birthday = input("Date of Birth: ")
    try:
        year, month, day = birthday.split("-")
        birthday = date(int(year), int(month), int(day))
        today = date.today()
        difference = (today - birthday).days
    except ValueError:
        sys.exit("Invalid date")
    print(time(difference))

def time(difference):
    minutes = difference * 24 * 60
    text = p.number_to_words(minutes, andword = "").capitalize()
    return f"{text} minutes"

if __name__ == "__main__":
    main()
