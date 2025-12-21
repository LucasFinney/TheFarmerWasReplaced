from __builtins__ import *

###Helper functions for preparing and farming the field.

# These functions operate on the current drone position and assume the caller
# moves the drone appropriately (the scripts in this repo iterate rows/cols
# and call these helpers while moving the drone).
###

def ensure_tree():
	###Plant a tree if there isn't one already.###
	if get_entity_type() != Entities.Tree:
		plant(Entities.Tree)


def ensure_bush():
	###Plant a bush if there isn't one already.###
	if get_entity_type() != Entities.Bush:
		plant(Entities.Bush)


def ensure_carrot():
	###Ensure soil is tilled and a carrot is planted.###
	if get_ground_type() != Grounds.Soil:
		till()
	if get_entity_type() != Entities.Carrot:
		plant(Entities.Carrot)


def prepare_tile(col, row):
	###Prepare a single tile based on repeating column pattern.

	# Pattern (col % 3):
	#   0 -> alternating grass/tree (tree on odd rows)
	#   1 -> alternating tree/bush (tree on even rows, bush on odd rows)
	#   2 -> carrots (till once and plant)
	###
	c = col % 3
	if c == 0:
		if row % 2 == 1:
			ensure_tree()
	elif c == 1:
		if row % 2 == 0:
			ensure_tree()
		else:
			ensure_bush()
	else:
		ensure_carrot()


def prepare_field(size):
	###Do a full preparation pass for an NxN field.###
	for i in range(size):
		for j in range(size):
			prepare_tile(i, j)
			move(North)
		move(East)


def farm_pass(size):
	###Perform a single farming pass: harvest and replant as appropriate.###
	for i in range(size):
		for j in range(size):
			col = i % 3
			if can_harvest():
				harvest()
				if col == 0 and j % 2 == 1:
					ensure_tree()
				elif col == 1:
					if j % 2 == 0:
						ensure_tree()
					else:
						ensure_bush()
				elif col == 2:
					# if soil was reset, re-till; then plant carrot
					if get_ground_type() != Grounds.Soil:
						till()
					ensure_carrot()
			move(North)
		move(East)


# --- Pumpkin helpers -------------------------------------------------------

def ensure_pumpkin():
	# """Ensure soil is tilled and a pumpkin is planted on the current tile.

	# Pumpkins behave like carrots: they require tilling before planting.
	# This helper is idempotent (safe to call repeatedly).
	# """
	if get_ground_type() != Grounds.Soil:
		till()
	if get_entity_type() != Entities.Pumpkin:
		plant(Entities.Pumpkin)


def prepare_pumpkin_field(size):
	# """Prepare an NxN field dedicated to pumpkins.

	# This tills and plants pumpkins on every tile in the field.
	# """
	for i in range(size):
		for j in range(size):
			ensure_pumpkin()
			move(North)
		move(East)


def farm_pass_pumpkins(size):
	# """Perform a single farming pass for pumpkins: harvest and replant."""
	for i in range(size):
		for j in range(size):
			if can_harvest():
				harvest()
				# replant pumpkin if necessary
				if get_entity_type() != Entities.Pumpkin:
					ensure_pumpkin()
			move(North)
		move(East)
