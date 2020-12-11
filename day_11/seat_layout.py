from functools import partial

class SeatLayout():
    
    def __init__(self, rows=[]):
        self.rows = rows
    
    def __str__(self):
        output = ""
        for row in self.rows:
            for seat in row:
                output += str(seat)
            output += '\n'
        return output
            
    def set_empty(self, seat):
        seat.empty()
        
    def set_occupied(self, seat):
        seat.occupy()
      
    def adjacent_sitters(self, row, col):
        count = 0
        for i in range(max(0, row-1), min(row+2, len(self.rows))):
            for j in range(max(0, col-1), min(col+2, len(self.rows[i]))):
                if (row != i or col != j) and self.rows[i][j].is_occupied():
                    count += 1
        return count
    
    def visible_sitters(self, row, col):
        visibles = []
        directions = [(i,j) for i in range(-1,2) for j in range(-1,2) if (i!=0 or j!=0)]
        steps = 0
        still_checking = True
        while directions and still_checking: 
            steps += 1
            directions_to_remove = []
            still_checking = False
            for d in directions:    
                x = row + d[0] * steps
                y = col + d[1] * steps                
                if 0 <= x < len(self.rows) and 0 <= y < len(self.rows[0]):
                    still_checking = True
                    space = self.rows[x][y]
                    if not space.is_floor():
                        visibles.append(space.code)
                        directions_to_remove.append(d)
            for dtr in directions_to_remove:
                directions.remove(dtr)
        return visibles.count('#')       
    
    def make_static_part_1(self):
        count = 0
        while True:
            count += 1
            changes = []
            for i, row in enumerate(self.rows):
                for j in range(len(row)):
                    seat = self.rows[i][j]
                    if seat.is_empty() and self.adjacent_sitters(i, j) == 0:
                        changes.append(partial(self.set_occupied, self.rows[i][j]))
                    elif seat.is_occupied() and self.adjacent_sitters(i, j) >= 4:
                        changes.append(partial(self.set_empty, self.rows[i][j]))
            if changes:
                for change in changes:
                    change()
                # print("Pass number " + str(count) + " " + str(len(changes)) + " changes made")
                if count == 100:
                    break
            else:
                break
            
    def make_static_part_2(self):
        count = 0
        while True:
            count += 1
            changes = []
            for i, row in enumerate(self.rows):
                for j in range(len(row)):
                    seat = self.rows[i][j]
                    if seat.is_empty() and self.visible_sitters(i, j) == 0:
                        changes.append(partial(self.set_occupied, self.rows[i][j]))
                    elif seat.is_occupied() and self.visible_sitters(i, j) >= 5:
                        changes.append(partial(self.set_empty, self.rows[i][j]))
            if changes:
                for change in changes:
                    change()
                # print("Pass number " + str(count) + " " + str(len(changes)) + " changes made")
                if count == 100:
                    break
            else:
                break