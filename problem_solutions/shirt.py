import sys
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    extension_list = ["png", "jpg", "jpeg"]
    if sys.argv[1].split(".")[1] in extension_list:
        if sys.argv[2].split(".")[1] in extension_list:
            if sys.argv[1].split(".")[1] == sys.argv[2].split(".")[1]:
                try:
                    image = Image.open(sys.argv[1])
                    shirt = Image.open("shirt.png")
                    size = shirt.size
                    puppet = ImageOps.fit(image, size)
                    puppet.paste(shirt, shirt)
                    puppet.save(sys.argv[2])
                except FileNotFoundError:
                    sys.exit("Input does not exist")
            else:
                sys.exit("Input and output have different extensions")
        else:
            sys.exit("Invalid output")
    else:
        sys.exit("Invalid input")
