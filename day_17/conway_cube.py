from functools import partial

class ConwayCube():
    
    def __init__(self, is_active):
        self.is_active = is_active
    
    @classmethod
    def from_symbol(cls, symbol):
        return cls(True) if symbol == '#' else cls(False)
    
    def __repr__(self):
        return '#' if self.is_active else '.'
    
    def switch_on_next_turn(self, active_neighbours):

#        If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
#        If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.

        if self.is_active and (active_neighbours < 2 or active_neighbours > 3):
            return True
        if not self.is_active and active_neighbours == 3:
            return True
        return False
    
#    def visible_sitters(self, row, col):
#        visibles = []
#        directions = [(i,j) for i in range(-1,2) for j in range(-1,2) if (i!=0 or j!=0)]
#        steps = 0
#        still_checking = True
#        while directions and still_checking: 
#            steps += 1
#            directions_to_remove = []
#            still_checking = False
#            for d in directions:    
#                x = row + d[0] * steps
#                y = col + d[1] * steps                
#                if 0 <= x < len(self.rows) and 0 <= y < len(self.rows[0]):
#                    still_checking = True
#                    space = self.rows[x][y]
#                    if not space.is_floor():
#                        visibles.append(space.code)
#                        directions_to_remove.append(d)
#            for dtr in directions_to_remove:
#                directions.remove(dtr)
#        return visibles.count('#')       
#    
