months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
        ]

while True:
    try:
        date = input("Date: ")
        if "/" in date:
            month, day, year = date.split("/")
        if "," in date:
            date = date.replace(",", "")
            month, day, year = date.split(" ")
            if month in months:
                month = months.index(month) + 1
        year = int(year)
        month = int(month)
        day = int(day)
        if month > 12 or day > 31:
            raise Exception
        else:
            print(f"{year}-{month:02}-{day:02}")
            break
    except:
        pass
