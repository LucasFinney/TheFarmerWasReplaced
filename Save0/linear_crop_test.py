from __builtins__ import *

# Use helper library and functions for clarity
clear()

from field_lib import prepare_field_linear, farm_pass_linear

# Preparation pass (run once), then continuous farming loop
size = get_world_size()
crops = [Entities.Grass, Entities.Bush, Entities.Tree]
prepare_field_linear(size, crops)
while True:
	farm_pass_linear(size, crops)
		