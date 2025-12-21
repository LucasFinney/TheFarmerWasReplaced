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


# Generic helpers ---------------------------------------------------------

def needs_till(entity):
	# """Return True if the entity requires tilling before planting."""
	return entity in (Entities.Carrot, Entities.Pumpkin)


def ensure_entity(entity):
	# """Ensure the given entity is present on the current tile
	# If the entity requires tilling, till first. This function is idempotent.
	# """
	if needs_till(entity) and get_ground_type() != Grounds.Soil:
		till()
	if get_entity_type() != entity:
		plant(entity)


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


def prepare_field(size, primary_crop=None):
	# """Do a full preparation pass for an NxN field.

	# If `primary_crop` is None the original mixed-column pattern is used.
	# If `primary_crop` is provided, every tile is prepared/seeded with that crop.
	# """
	for i in range(size):
		crop = i % len(primary_crop)
		for j in range(size):
			if primary_crop == None:
				prepare_tile(i, j)
			else:
				ensure_entity(primary_crop[crop])
			move(North)
		move(East)

def default_mix(size,i,j):
	# """Prepare the default mixed crop pattern for an NxN field."""
	if i % 3 ==0 and j % 2 == 1:
		ensure_tree()
	elif i % 3 == 1:
		if j % 2 == 0:
			ensure_tree()
		else:
			ensure_bush()
	elif i % 3 == 2:
		# if soil was reset, re-till; then plant carrot
		if get_ground_type() != Grounds.Soil:
			till()
		ensure_carrot()

def farm_pass(size, primary_crop=None):
	# Perform a single farming pass.

	# If `primary_crop` is None, the original mixed pattern is used where columns
	# cycle grass/tree, tree/bush, and carrots. If `primary_crop` is provided,
	# the farm is treated as dedicated to that crop (pumpkins, carrots, etc.).
	# If primary_crop is a list, then iterate through the list for planting.
	for i in range(size):
		for j in range(size):
			crop = i % len(primary_crop)
			if can_harvest():
				harvest()
				if primary_crop == None:
					default_mix(size,i,j)
				else:
					# dedicated crop: ensure it is replanted/tiled appropriately
					ensure_entity(primary_crop[crop])
			# if not harvesting, check for unused tiles in dedicated crop mode
			elif primary_crop != None:
				ensure_entity(primary_crop[crop])
			move(North)
		move(East)


def prepare_field_linear(size, primary_crop=None):
	# """Prepare an NxN field using a linear repeating sequence of crops.

	# Traversal order matches the original helpers (column-major travel: move
	# North across a column, then East to the next column). If `primary_crop`
	# is a list, its elements are used in sequence for every tile traversed;
	# if a single entity is passed (for backward compatibility), that entity is
	# used for every tile.
	# """
	if primary_crop is None:
		for i in range(size):
			for j in range(size):
				prepare_tile(i, j)
				move(North)
			move(East)
	else:
		# single entity: treat as dedicated crop for entire field
		if not hasattr(primary_crop, "__len__") or not hasattr(primary_crop, "__getitem__"):
			for i in range(size):
				for j in range(size):
					ensure_entity(primary_crop)
					move(North)
				move(East)
		else:
			k = 0
			for i in range(size):
				for j in range(size):
					crop = primary_crop[k % len(primary_crop)]
					ensure_entity(crop)
					k += 1
					move(North)
				move(East)


def farm_pass_linear(size, primary_crop=None):
	# """Perform a single farming pass using a linear repeating sequence of crops.

	# For `primary_crop` lists, the k-th tile visited (column-major ordering)
	# uses `primary_crop[k % len(primary_crop)]`. If a single entity is passed,
	# that entity is used for every tile. When `primary_crop` is None the
	# original `default_mix` behaviour is used after harvesting.
	# """
	for i in range(size):
		for j in range(size):
			k = i * size + j
			if primary_crop is None:
				if can_harvest():
					harvest()
					default_mix(size, i, j)
			else:
				# single entity support
				if not hasattr(primary_crop, "__len__") or not hasattr(primary_crop, "__getitem__"):
					crop = primary_crop
				else:
					crop = primary_crop[k % len(primary_crop)]
				if can_harvest():
					harvest()
					ensure_entity(crop)
				else:
					ensure_entity(crop)
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
	# """Backward-compatible API: prepare an NxN pumpkin field using the
	# general `prepare_field` helper under the hood."""
	prepare_field(size, Entities.Pumpkin)


def farm_pass_pumpkins(size):
	# """Backward-compatible API: single-pass pumpkin farming using generic helper."""
	farm_pass(size, Entities.Pumpkin)


# --- Test helpers ---------------------------------------------------------

def run_once(size, primary_crop=None, prepare=True, farm=True):
	# """Run a single prepare and/or farm pass and then stop.

	# This is useful for testing changes in-game without leaving a continuous
	# `while True` loop running. Example usages:
	
	# # Prepare a dedicated pumpkin field and do a single farming pass
	# from field_lib import run_once
	# size = get_world_size()
	# run_once(size, Entities.Pumpkin)

	# # Run only a single farm pass on the existing field
	# run_once(size, primary_crop=None, prepare=False, farm=True)
	# """
	if prepare:
		prepare_field(size, primary_crop)
	if farm:
		farm_pass(size, primary_crop)
