class Instruction():
    
    def __init__(self, op, arg):
        self.op = op
        self.arg = arg
        self.is_active = False
      
    def enact_instruction(self, acc):
        self.is_active = True
        if self.op == "acc":
            return acc + self.arg
        else:
            return acc
          
    def get_next_instruction(self, current_pos):
        if self.op == "jmp":
            return current_pos + self.arg
        else:
            return current_pos + 1
            