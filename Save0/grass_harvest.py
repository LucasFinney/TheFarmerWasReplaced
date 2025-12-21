# Prepare a farm of just grass
from __builtins__ import *
clear()
from field_lib import prepare_field, farm_pass
size= get_world_size()
prepare_field(size, [Entities.Grass])
while True:
	farm_pass(size, [Entities.Grass])