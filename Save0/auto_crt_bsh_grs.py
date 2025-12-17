from __builtins__ import *

clear()

# auto_crt_bsh_grs.py
# Preparation pass (run once):
#  - Column 0: grass (leave)
#  - Column 1: plant bushes on every tile
#  - Column 2: till once and plant carrots on every tile

# prepare the farm (3x3 fixed)
for i in range(3):
	for j in range(3):
		if i == 0:
			pass
		elif i == 1:
			plant(Entities.Bush)
		else:
			# till once, then plant carrots
			till()
			plant(Entities.Carrot)
		move(North)
	move(East)

# Farming loop: harvest when ready and replant (do not retill carrots)
while True:
	for i in range(3):
		for j in range(3):
			if can_harvest():
				harvest()
				# replant according to column
				if i == 1:
					plant(Entities.Bush)
				elif i == 2:
					plant(Entities.Carrot)
			move(North)
		move(East)
