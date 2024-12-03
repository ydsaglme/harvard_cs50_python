expression = input("Expression: ")
x, y, z = expression.strip().split(" ")

if y == "+":
    print(float(x)+float(z))
elif y == "-":
    print(float(x)-float(z))
elif y == "*":
    print(float(x)*float(z))
elif y == "/":
    print(float(x)/float(z))
