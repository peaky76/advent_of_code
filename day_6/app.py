file = open("puzzle_input.txt", "r")
groups = [[]]

for line in file:
    line = line.rstrip('\n')
    if line: #Add details to current group
        groups[len(groups) - 1].append(line)    
    else: #Start a new group
        groups.append([])
        
def any_answer_yes_count(group):
    return len(set(''.join(group)))

def all_answer_yes_count(group):
    return len([answer for answer in set(''.join(group)) if all(answer in person for person in group)])

part_1_answer = sum(any_answer_yes_count(group) for group in groups)
part_2_answer = sum(all_answer_yes_count(group) for group in groups)
print("Part 1: " + part_1_answer + " Part 2: " + part_2_answer)