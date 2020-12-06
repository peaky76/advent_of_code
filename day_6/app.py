file = open("puzzle_input.txt", "r")
groups = [[]]

for line in file:
    line = line.rstrip('\n')
    if line:
        #Add details to current group
        groups[len(groups) - 1].append(line)    
    else:
        #Start a new group
        groups.append([])
        
#PART ONE
def any_answer_yes_count(group):
    return len(set(''.join(group)))

answer = sum(any_answer_yes_count(group) for group in groups)
print(answer)

#PART TWO
def all_answer_yes_count(group):
    return len([answer for answer in set(''.join(group)) if all(answer in person for person in group)])

answer = sum(all_answer_yes_count(group) for group in groups)
print(answer)