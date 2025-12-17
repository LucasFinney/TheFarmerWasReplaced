from __builtins__ import *

clear()

# auto_crt_bsh_grs.py
# 3x3 farm only: use iterators `i` (column) and `j` (row) — no variable assignment allowed.
# Layout per 3-column group:
#   i==0 -> grass (leave)
#   i==1 -> bushes
#   i==2 -> carrots (till then plant)

while True:
	# columns i = 0..2
	for i in range(3):
		# rows j = 0..2 (fixed 3x3 farm)
		for j in range(3):
			if can_harvest():
				harvest()

			if i == 0:
				# grass column: nothing to do
				pass
			elif i == 1:
				# bush column: plant on checker pattern
				if (i + j) % 2 == 0:
					plant(Entities.Bush)
			else:
				# carrot column: till then plant on checker pattern
				if (i + j) % 2 == 0:
					till()
					plant(Entities.Carrot)

			move(North)
		move(East)
