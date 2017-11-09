#notes = {'£50': 0, '£20': 0, '£10' : 0, '£5' : 0, '£2' : 0, '£1' : 0}

coins = [5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]


Amount = float(input("Price of item: "))
Paid = float(input("How much paid: "))
change = int((Paid - Amount) * 100)

for i in range(len(coins)):
    left = change // coins[i]
    if left > 0:
        print((coins[i] / 100), left)
        change -= left * coins[i]
