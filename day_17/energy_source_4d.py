from conway_cube import ConwayCube
import pprint

class EnergySource4d():
    
    def __init__(self, flat_region):
        self.cubes = {}
        self.cycles = 0
        self.orig_y = len(flat_region)
        self.orig_x = len(flat_region[0])
        for a, row in enumerate(flat_region):
            for b, symbol in enumerate(row):
                self.cubes[(0,0,a,b)] = ConwayCube.from_symbol(symbol)
    
    def adjacent_active_cubes(self, w, z, y, x):
        count = 0
        for l in range(max(0 - self.cycles, w-1), min(w+2, self.cycles + 1)):
            for k in range(max(0 - self.cycles, z-1), min(z+2, self.cycles + 1)):
                for j in range(max(0 - self.cycles, y-1), min(y+2, self.cycles + self.orig_y)):
                    for i in range(max(0 - self.cycles, x-1), min(x+2, self.cycles + self.orig_x)):
                        if (l, k, j, i) in self.cubes.keys() and self.cubes[(l, k, j, i)].is_active:
                            if l != w or k != z or j != y or i != x:
                                count += 1                       
        return count
                         
    def run_cycle(self):
        self.cycles += 1
        print("Running cycle " + str(self.cycles))
        cubes_to_switch = []
        for w in range(0 - self.cycles, self.cycles + 1):
            for z in range(0 - self.cycles, self.cycles + 1):
                for y in range(0 - self.cycles, self.cycles + self.orig_y):
                    for x in range(0 - self.cycles, self.cycles + self.orig_x):
                        adjs = self.adjacent_active_cubes(w, z, y, x)
                        if (w, z, y, x) not in self.cubes.keys():
                            self.cubes[(w, z, y, x)] = ConwayCube(False)
                        cube = self.cubes[(w, z, y, x)]
                        if cube.switch_on_next_turn(adjs):
                            cubes_to_switch.append(cube)
        for cube in cubes_to_switch:
            cube.is_active = not cube.is_active