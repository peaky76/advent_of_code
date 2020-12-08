from instruction import Instruction

file = open("puzzle_input.txt", "r")
instructions = []

for line in file:
    line = line.rstrip('.\n')
    op, arg = line.split(' ')
    instructions.append(Instruction(op, int(arg)))

def run_prog(instruction_set):
    hit_infinite_loop = False
    curr_idx = 0
    acc = 0
    
    while not hit_infinite_loop and not curr_idx + 1 == len(instruction_set):
        acc += instruction_set[curr_idx].get_increment()
        curr_idx += instruction_set[curr_idx].get_next_move()
        hit_infinite_loop = instruction_set[curr_idx].is_active
       
    return (not hit_infinite_loop, acc)

# PART ONE
print(run_prog(instructions))

# PART TWO    
def get_fault_corrected_output(instructions):
    for idx, instruction in enumerate(instructions):
        swapped_instruction_op = None
        if instruction.op == "nop":
            swapped_instruction_op = "jmp"
        if instruction.op == "jmp":
            swapped_instruction_op = "nop"
        if swapped_instruction_op:
            modified_instructions = instructions[:idx] + [Instruction(swapped_instruction_op, instruction.arg)] + instructions[idx+1:]
            for instruction in modified_instructions:
                instruction.is_active = False
            test = run_prog(modified_instructions)
            if test[0] == True:
                return test[1]
            
print(get_fault_corrected_output(instructions))