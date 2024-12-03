coke = 50
remained = coke
coins = [5, 10, 25]

while remained > 0:
    print("Amount Due: " + str(remained))
    inserted_coin = int(input("Insert Coin: "))
    if inserted_coin in coins:
        remained = remained - inserted_coin
    else:
        continue

if remained < 0:
    remained = -remained

print("Change Owed: " + str(remained))