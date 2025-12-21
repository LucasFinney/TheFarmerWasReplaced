from __builtins__ import *

# Use helper library and functions for clarity
clear()

from field_lib import prepare_field, farm_pass

# Preparation pass (run once), then continuous farming loop
size = get_world_size()
prepare_field(size, Entities.Pumpkin)

while True:
	farm_pass(size, Entities.Pumpkin)
		