camel = input("camelCase: ")
snake = print("snake_case: ", end = "")

for character in camel:
    if character.islower():
        print(character, sep = "", end = "")
    else:
        print("_", character.lower(), sep = "", end = "")