import random

def main():
    equations = 10
    attempts = 3
    score = 0
    level = get_level()
    while equations > 0:
        if attempts == 3:
            a, b = generate_integer(level)
        try:
            response = input(f"{a} + {b} = ")
            if int(response) == (a + b):
                equations -= 1
                score += 1
                attempts = 3
                continue
            else:
                raise ValueError
        except:
            attempts -= 1
            print("EEE")
            pass
        if attempts == 0:
            print((f"{a} + {b} = {a + b}"))
            equations -= 1
            attempts = 3
            continue
    print("Score:", score)

def get_level():
    levels = [1, 2, 3]
    while True:
        try:
            level = int(input("Level: "))
            if level in levels:
                return level
        except:
            pass

def generate_integer(level):
    if level == 1:
        a = random.randint(0, 9)
        b = random.randint(0, 9)
    elif level == 2:
        a = random.randint(10, 99)
        b = random.randint(10, 99)
    else:
        a = random.randint(100, 999)
        b = random.randint(100, 999)
    return a, b

if __name__ == "__main__":
    main()
