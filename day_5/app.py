file = open("puzzle_input.txt", "r")
boarding_passes = []
seat_ids = []

for line in file:
    boarding_passes.append(line.rstrip('\n'))
    
for bp in boarding_passes:
    row = int(bp[:7].replace('B', '1').replace('F', '0'), 2)
    col = int(bp[7:].replace('R', '1').replace('L', '0'), 2)
    seat_id = row * 8 + col
    seat_ids.append(seat_id)
    
# PART ONE ANSWER    
print(max(seat_ids))
    
# PART TWO ANSWER
for i in range(min(seat_ids), max(seat_ids)):
    if i not in seat_ids:
        print(i)