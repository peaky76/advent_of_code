import time
from movement import Movement

file = open("puzzle_input.txt", "r")
instructions = []

for line in file:
    line = line.rstrip('\n')
    instructions.append(line)
        
def get_manhattan_distance(start_move, instructions, waypoint=False):
    
    northness = 0
    eastness = 0 

    for instruction in instructions:    
        command = instruction[0]
        amount = int(instruction[1:])
        if command in ['L', 'R']:
            curr_move.rotate(command, amount)        
        else:
            if command == 'F':
                change_to_position = curr_move.apply(amount)
            else:
                if waypoint:
                    curr_move.modify(Movement.specify(command).apply(amount))
                    change_to_position = None
                else:
                    change_to_position = Movement.specify(command).apply(amount)
            if change_to_position:            
                eastness += change_to_position.eastwards
                northness += change_to_position.northwards

    return abs(eastness) + abs(northness)    

# PART ONE
curr_move = Movement.specify('E')
print(get_manhattan_distance(curr_move, instructions))

# # PART TWO
curr_move = Movement(10, 1)
print(get_manhattan_distance(curr_move, instructions, waypoint=True))
