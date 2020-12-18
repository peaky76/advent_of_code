from energy_source_4d import EnergySource4d
from conway_cube import ConwayCube

import numpy
import pprint
import time

file = open("puzzle_input.txt", "r")

rows = [list(line.rstrip('\n')) for line in file]

model = EnergySource4d(rows)
pprint.pprint(model.cubes)

for i in range(6):
    tic = time.perf_counter()
    model.run_cycle()
    toc = time.perf_counter()
    print("Cycle " + str(i + 1) + " completed in " + str(toc-tic) + " secs")
    print(sum(1 for coords, cube in model.cubes.items() if cube.is_active))