from itertools import combinations

file = open("puzzle_input.txt", "r")
xmas_cypher = []

for line in file:
    line = line.rstrip('.\n')
    xmas_cypher.append(int(line))
  
def is_next_num_valid(preamble, next_num):
    return next_num in [x + y for x, y in combinations(preamble, 2)]

def get_first_invalid_num(cypher):
    preamble_end = 25
    while preamble_end <= len(cypher):    
        preamble = cypher[preamble_end - 25:preamble_end]
        if is_next_num_valid(preamble, cypher[preamble_end]):
            preamble_end += 1
        else:
            return cypher[preamble_end]
        
def find_weakness_exploit_for_invalid_num(cypher, invalid_num):
    for i, num in enumerate(cypher):
        sum = num
        for j in range(i + 1, len(cypher)):
            sum += cypher[j]
            if sum == invalid_num:
                return min(cypher[i:j]) + max(cypher[i:j])
            if sum > invalid_num:
                break    

invalid_num = get_first_invalid_num(xmas_cypher)
exploit = find_weakness_exploit_for_invalid_num(xmas_cypher, invalid_num)

print(str(invalid_num) + " can be exploited with " + str(exploit))