grocery_list = {}

while True:
    try:
        get_item = input().upper()
    except EOFError:
        break
    except:
        pass
    else:
        if get_item in grocery_list:
            grocery_list[get_item] = grocery_list[get_item] + 1
        else:
            grocery_list[get_item] = 1

for key in sorted(grocery_list.keys()):
    print(grocery_list[key], key)