from __builtins__ import *

# Experiment: auto-harvest prototype
# - Safe, small change that demonstrates an experimental branch.

def auto_harvest(steps):
    """Move forward up to `steps` times, harvesting if possible."""
    for _ in range(steps):
        if can_harvest():
            harvest()
        else:
            move(North)


# Keep the original movement behaviour for comparison
for i in range(2):
    for j in range(get_world_size()):
        move(North)
    move(East)

# Run a short auto-harvest test (no-op if harvest not available)
auto_harvest(3)
