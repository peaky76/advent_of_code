class Movement():
    
    def __init__(self, eastwards, northwards):
        self.eastwards = eastwards
        self.northwards = northwards
        
    @classmethod    
    def specify(cls, compass_code):
        COMPASS = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
        return cls(*COMPASS[compass_code])
    
    def modify(self, movement):
        self.eastwards += movement.eastwards
        self.northwards += movement.northwards
    
    def rotate(self, direction, num_of_degrees):
        turns = num_of_degrees // 90
        if direction == "R":
            for i in range(turns):
                self.eastwards, self.northwards = self.northwards, -self.eastwards 
        if direction == "L":
            for i in range(turns):
                self.eastwards, self.northwards = -self.northwards, self.eastwards
               
    def apply(self, num_of_moves=1):
        return {'eastwards': self.eastwards * num_of_moves,
                'northwards': self.northwards * num_of_moves}
    
