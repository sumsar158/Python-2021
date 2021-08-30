"""Cha-ching!"""
amount = int(input("Enter a sum: "))
coins = []
cents = [1, 5, 10, 20, 50]

for cent in sorted(cents, reverse=True):
    whole_number = amount // cent
    amount = amount % cent
    coins.append(whole_number)
coins_sum = sum(coins)

print(f"Amount of coins needed: {coins_sum}")
