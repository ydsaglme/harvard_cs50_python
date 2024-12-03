import inflect

name_list = list()
p = inflect.engine()

while True:
    try:
        name = input("Name: ")
        name_list.append(name)
    # CTRL + D raises an EOFError.
    except EOFError:
        break

names = p.join(name_list)
print("Adieu, adieu, to", names)