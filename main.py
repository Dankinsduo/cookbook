cook_book = {}
with open('file.py') as f:
  for line in f:
    dish = line.strip()
    quantity = int(f.readline())
    ingredients = []
    for i in range(quantity):
      ingredient = f.readline().strip().split(' | ')
      ingredients.append(ingredient)
      cook_book[dish] = ingredients
    f.readline()
import pprint 
pprint.pprint(cook_book)