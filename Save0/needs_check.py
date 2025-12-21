# Check which items need to be planted
from __builtins__ import *
items = [Items.Hay, Items.Wood, Items.Carrot, Items.Pumpkin]
to_plant = []
for i in items:
	if num_items(i) < 1000:
		to_plant.append(i)
print(to_plant)