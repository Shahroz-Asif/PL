import random

items = { "eggs", "milk", "sugar", "coffee", "tea", "bread" }
prices = {
    "eggs": 120,
    "milk": 220,
    "sugar": 300,
    "coffee": 510,
    "tea": 240,
    "bread": 140
}

print("Items initially available: ", items)
print("Items with their prices: ", prices)

amount_sold = random.randint(3, len(items))
sold_items = []

for i in range(amount_sold):
    sold_items.append(items.pop())

sold_item_prices = [ prices[item] for item in sold_items ]

max_price = max(sold_item_prices)
max_price_index = sold_item_prices.index(max_price)

min_price = min(sold_item_prices)
min_price_index = sold_item_prices.index(min_price)

print("Amount of items sold: " + str(len(sold_items)))
print("Max priced item sold: " + sold_items[max_price_index] + " for " + str(max_price))
print("Min priced item sold: " + sold_items[min_price_index] + " for " + str(min_price))