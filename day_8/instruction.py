class Instruction():
    
    def __init__(self, op, arg):
        self.op = op
        self.arg = arg
        self.is_active = False
        
    def __repr__(self):
        return self.op + ' ' + str(self.arg)
      
    def get_increment(self):
        self.is_active = True
        if self.op == "acc":
            return self.arg
        else:
            return 0
          
    def get_next_move(self):
        if self.op == "jmp":
            return self.arg
        else:
            return 1
            