menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0

while True:
    try:
        get_item = input("Item: ").lower().title()
        if get_item in menu:
            get_item
        else:
            raise Exception
    except EOFError:
        break
    except:
        pass
    else:
        total = total + menu[get_item]
        print(f"${total:.2f}$")
