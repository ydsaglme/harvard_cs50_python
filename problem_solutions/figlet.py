from pyfiglet import Figlet
import sys

figlet = Figlet()
fonts = figlet.getFonts()
first_command_line = ["-f", "--font"]

if len(sys.argv) == 1:
    isRandom = True
elif len(sys.argv) == 3 and sys.argv[1] in first_command_line:
    isRandom = False
else:
    print("Invalid usage")
    sys.exit(1)

if isRandom == False:
    try:
        figlet.setFont(font = sys.argv[2])
    except:
        print("Invalid usage")
        sys.exit(1)
else:
    pass

text = input("Input: ")
print("Output:",(figlet.renderText(text)))