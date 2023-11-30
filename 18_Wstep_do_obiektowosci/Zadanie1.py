# Zadania

# - Stworzyć klasę `FoodItem` z polami `id`, `price` `item` - specjalnymi metodami `__init__` i `__repr__`,
# stworzyć listę `FoodItem` na podstawie pliku CSV

import csv
class FoodItems:

    def __init__(self, id, price, item):
        self.id = id
        self.price = price
        self.item = item
    def __repr__(self):
        return f'FoodItems("{self.id}", "{self.price}", "{self.item}")'

with open('foods.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)