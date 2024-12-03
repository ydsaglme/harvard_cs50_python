answer = input("What is the the Answer to the Great Question of Life, the Universe and Everything? ")
ans = answer.strip().lower()

if ans == "42" or ans == "forty two" or ans == "forty-two":
    print("Yes")
else:
    print("No")
