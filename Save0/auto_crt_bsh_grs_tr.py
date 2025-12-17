from __builtins__ import *

clear()

# auto_crt_bsh_grs.py
# Preparation pass (run once):
#  - Column 0: alternate grass and trees (leave grass, plant tree if none)
#  - Column 1: alternate trees and bushes (plant tree if none, else bush)
#  - Column 2: till once and plant carrots on every tile

# prepare the farm (dynamic size using in-game `get_world_size()`)
size = get_world_size()
for i in range(size):
	for j in range(size):
		# columns repeat in groups of three: 0=grass, 1=bush, 2=carrot
		col = i % 3
		if col == 0 and j % 2 == 0:
			# grass column: leave as-is
			pass
		elif col == 0 and j % 2 == 1:
			# tree column: plant a tree only if not already present
			if get_entity_type() != Entities.Tree:
				plant(Entities.Tree)
		elif col == 1 and j % 2 == 0:
			# tree column: plant a tree only if not already present
			if get_entity_type() != Entities.Tree:
				plant(Entities.Tree)
		elif col == 1 and j % 2 == 1:
			# bush column: plant a bush only if not already present
			if get_entity_type() != Entities.Bush:
				plant(Entities.Bush)
		else:
			# carrot column: ensure soil is tilled once, then plant carrots
			if get_ground_type() != Grounds.Soil:
				till()
			if get_entity_type() != Entities.Carrot:
				plant(Entities.Carrot)
		move(North)
	move(East)

# Farming loop: harvest when ready and replant (do not retill carrots unless soil is lost)
while True:
	for i in range(size):
		for j in range(size):
			col = i % 3
			if can_harvest():
				harvest()
				if col == 0 and j % 2 == 1:
					# tree column: plant a tree only if not already present
					if get_entity_type() != Entities.Tree:
						plant(Entities.Tree)
				elif col == 1 and j % 2 == 0:
					# tree column: plant a tree only if not already present
					if get_entity_type() != Entities.Tree:
						plant(Entities.Tree)
				elif col == 1 and j % 2 == 1:
					# bush column: plant a bush only if not already present
					if get_entity_type() != Entities.Bush:
						plant(Entities.Bush)
				elif col == 2:
					# if soil was reset, till again
					if get_ground_type() != Grounds.Soil:
						till()
					if get_entity_type() != Entities.Carrot:
						plant(Entities.Carrot)
			move(North)
		move(East)
		