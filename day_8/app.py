from instruction import Instruction
from instruction_set import InstructionSet

file = open("puzzle_input.txt", "r")
instructions = []

for line in file:
    line = line.rstrip('.\n')
    op, arg = line.split(' ')
    instructions.append(Instruction(op, int(arg)))

# PART ONE
print(InstructionSet(instructions).acc)

# PART TWO    
for idx, instruction in enumerate(instructions):
    swapped_instruction_op = None
    if instruction.op == "nop":
        swapped_instruction_op = "jmp"
    if instruction.op == "jmp":
        swapped_instruction_op = "nop"
    if swapped_instruction_op:
        modified_instructions = InstructionSet(instructions[:idx] + [Instruction(swapped_instruction_op, instruction.arg)] + instructions[idx+1:])            
        if modified_instructions.is_valid:
            print(modified_instructions.acc)