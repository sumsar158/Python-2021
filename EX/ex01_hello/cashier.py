"""Cha-ching."""
amount = int(input("Enter a sum: "))
coins_list = []
cents = [1, 5, 10, 20, 50]

for cent in sorted(cents, reverse=True):
    coins = amount // cent
    amount %= cent
    coins_list.append(coins)

coins_sum = sum(coins_list)

print(f"Amount of coins needed: {coins_sum}")
