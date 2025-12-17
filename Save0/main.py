from __builtins__ import *
clear()
while True:
	for i in range(3):
		for j in range(get_world_size()):
			# if can_harvest():
			# harvest()
			if (i+j)%2==0:
				plant(Entities.Bush)
			move(North)
		move(East)