class BagRule():
    
    def __init__(self, color):
        self.outer = color
        self.inners = {}
              
    def add_inner(self, color, num):
        self.inners.update({color: num})