class SeatSpace():
    
    def __init__(self, code):
        self.code = code
        
    def is_empty(self):
        return self.code == 'L'
    
    def is_floor(self):
        return self.code == '.'
    
    def is_occupied(self):
        return self.code == '#'
    
    def occupy(self):
        if self.code == 'L':
            self.code == '#'
            
    def unoccupy(self):
        if self.code == '#':
            self.code == 'L'