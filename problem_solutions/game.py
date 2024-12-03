import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except:
        pass

random_integer = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess < random_integer:
                print("Too small!")
            elif guess > random_integer:
                print("Too large!")
            else:
                print("Just right!")
                break
    except:
        pass