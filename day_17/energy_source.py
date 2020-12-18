from conway_cube import ConwayCube
import pprint

class EnergySource():
    
    def __init__(self, flat_region):
        self.cubes = [[[ConwayCube(False) for i in range(len(flat_region[0]))] for j in range(len(flat_region))]]
        for a, row in enumerate(flat_region):
            for b, symbol in enumerate(row):
                self.cubes[0][a][b] = ConwayCube.from_symbol(symbol)
    
    def adjacent_active_cubes(self, z, y, x):
        count = 0
        for k in range(max(0, z-1), min(z+2, len(self.cubes))):
            for j in range(max(0, y-1), min(y+2, len(self.cubes[k]))):
                for i in range(max(0, x-1), min(x+2, len(self.cubes[k][j]))):
                    if self.cubes[k][j][i].is_active:
                        if k != z or j != y or i != x:
                            count += 1                       
        return count
    
    def expand_fields(self):
        new_z_len = len(self.cubes) + 2
        new_y_len = len(self.cubes[0]) + 2
        new_x_len = len(self.cubes[0][0]) + 2
        new_top_layer = [[ConwayCube(False) for i in range(new_x_len)] for j in range(new_y_len)]
        new_middle_layers = []
        for layer in self.cubes:
            new_middle_layer = [[ConwayCube(False) for i in range(new_x_len)],
                                *[[ConwayCube(False), *row, ConwayCube(False)] for row in layer],
                                [ConwayCube(False) for i in range(new_x_len)]]
            new_middle_layers.append(new_middle_layer)
        new_bottom_layer = [[ConwayCube(False) for i in range(new_x_len)] for j in range(new_y_len)]
        self.cubes = [new_top_layer, *new_middle_layers, new_bottom_layer]
         
    def run_cycle(self):
        self.expand_fields()
        cubes_to_switch = []
        for z, plane in enumerate(self.cubes):
            for y, row in enumerate(plane):
                for x, cube in enumerate(row):
                    adjs = self.adjacent_active_cubes(z, y, x)
                    if cube.switch_on_next_turn(adjs):
                        cubes_to_switch.append(cube)
        for cube in cubes_to_switch:
            cube.is_active = not cube.is_active