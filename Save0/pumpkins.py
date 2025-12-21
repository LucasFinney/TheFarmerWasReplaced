from __builtins__ import *

# Use helper library and functions for clarity
clear()

from field_lib import prepare_pumpkin_field, farm_pass_pumpkins

# Preparation pass (run once), then continuous farming loop
size = get_world_size()
prepare_pumpkin_field(size)

while True:
	farm_pass_pumpkins(size)
		