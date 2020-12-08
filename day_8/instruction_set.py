class InstructionSet():
    
    def __init__(self, instructions):
        self.instructions = instructions
        self.acc = 0
        self.is_valid = False
        self.__test()
        
    def __test(self):
        curr_idx = 0
        instructions_used = []
    
        while not curr_idx in instructions_used and not curr_idx + 1 == len(self.instructions):
            instructions_used.append(curr_idx)
            self.acc += self.instructions[curr_idx].get_increment()
            curr_idx += self.instructions[curr_idx].get_next_move()
            
        self.is_valid = curr_idx + 1 == len(self.instructions)