from __builtins__ import *

clear()

# auto_carrot.py
# Harvest and plant carrots in a grid pattern.
# Behavior:
# - Walk the farm in rows equal to `get_world_size()`.
# - If a tile can be harvested, harvest it.
# - Plant `Entities.Carrot` in a checkerboard pattern to reduce crowding.

def run_grid(rows=3, spacing=1):
    for i in range(rows):
        for j in range(get_world_size()):
            if can_harvest():
                harvest()
            # simple spacing/checkerboard: plant on alternating tiles
            if (i + j) % (2 * spacing) == 0:
                plant(Entities.Carrot)
            move(North)
        move(East)


# Main loop: repeat the grid pass indefinitely
while True:
    run_grid(rows=3, spacing=1)
