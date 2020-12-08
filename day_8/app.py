from instruction import Instruction

file = open("puzzle_input.txt", "r")
instructions = []

for line in file:
    line = line.rstrip('.\n')
    op, arg = line.split(' ')
    instructions.append(Instruction(op, int(arg)))

hit_infinite_loop = False
curr_idx = 0
acc = 0
    
while not hit_infinite_loop:
    acc = instructions[curr_idx].enact_instruction(acc)
    curr_idx = instructions[curr_idx].get_next_instruction(curr_idx)
    hit_infinite_loop = instructions[curr_idx].is_active
    
print(acc)    