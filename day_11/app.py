from seat_space import SeatSpace
from seat_layout import SeatLayout
import time

file = open("puzzle_input.txt", "r")
rows = []

for line in file:
    line = line.rstrip('\n')
    rows.append([SeatSpace(x) for x in list(line)])

# layout_1 = SeatLayout(rows)

# # PART ONE
# tic = time.perf_counter()    
# layout_1.make_static_part_1()
# toc = time.perf_counter()

# print(toc - tic)
# print(sum(1 for row in layout_1.rows for seat in row if seat.is_occupied()))


layout_2 = SeatLayout(rows)

#PART TWO
tic = time.perf_counter()    
layout_2.make_static_part_2()
toc = time.perf_counter()

print(toc - tic)
print(sum(1 for row in layout_2.rows for seat in row if seat.is_occupied()))
