from functools import reduce
from time import perf_counter

file = open("puzzle_input.txt", "r")
lines = [line for line in file]

curr_time = int(lines[0].rstrip('\n'))
all_buses = [bus for bus in lines[1].rstrip('\n').split(',')]
named_buses = [int(bus) for bus in all_buses if bus != 'x']

def next_arrival_time(bus, curr_time):
    return (curr_time // bus + 1) * bus

# def lcm(x, y):
    
#     counter = max(x,y)
#     while True:
#        if((counter % x == 0) and (counter % y == 0)):
#            break
#        counter += 1

#     return counter

def get_recurring_pattern(bus_a, bus_b):
    spacing = bus_a[0] * bus_b[0]
    max_bus, min_bus = sorted([bus_a, bus_b], reverse=True)
    # tac = perf_counter()
    multiple = min_bus[0] - (max_bus[1] % min_bus[0] - min_bus[1])
    if multiple == 0:
        multiple = min_bus[0]
    multiple = 1
    while (max_bus[0] * multiple - max_bus[1] + min_bus[1]) % min_bus[0] != 0:
        multiple += 1
    # tuc = perf_counter()
    # print(tuc - tac)
    first_occurrence = max_bus[0] * multiple - max_bus[1]
    if first_occurrence < 0:
        first_occurrence += spacing
    answer = (spacing, spacing - first_occurrence) 
    # print(answer)
    return answer

# print(get_recurring_pattern((3,0), (8,1))) #15, #24 (24, 9)    2    
# print(get_recurring_pattern((3,0), (8,2))) #6, #24 (24, 18)    1     
# print(get_recurring_pattern((3,0), (8,3))) #21, #24 (24, 3)    3    
# print(get_recurring_pattern((3,0), (8,4))) #12, #24            2          
# print(get_recurring_pattern((3,0), (8,5))) #3, #24             1

# print(get_recurring_pattern((2,0), (7,1))) #6, #14             1     
# print(get_recurring_pattern((2,0), (7,2))) #12, #14            2 
# print(get_recurring_pattern((2,0), (7,3))) #4, #14             1 
# print(get_recurring_pattern((2,0), (7,4))) #10, #14            2 
# print(get_recurring_pattern((2,0), (7,5))) #2, #14             1 

# print(get_recurring_pattern((3,1), (5,2))) #8, #15             2
# print(get_recurring_pattern((3,1), (5,3))) #2, #15             1
# print(get_recurring_pattern((3,1), (5,4))) #11, #15            3 

# print(get_recurring_pattern((4,3), (7,4)))                     #3               
# print(get_recurring_pattern((4,3), (7,5)))                     #2
# print(get_recurring_pattern((4,3), (7,6)))                     #1 

# print(get_recurring_pattern((7,4), (12,5))) #67
# print(get_recurring_pattern((6,1), (11,4))) #29        
        
# PART ONE
next_arrival_times = dict([(bus, next_arrival_time(bus, curr_time)) for bus in named_buses])
soonest_bus = min(next_arrival_times, key=next_arrival_times.get)
print(soonest_bus * (next_arrival_times[soonest_bus] - curr_time))

# PART TWO
tic = perf_counter()
time_offsets = [i for i, bus in enumerate(all_buses) if bus != 'x']
buses_and_offsets = sorted(list(zip(named_buses, time_offsets)), reverse=True)
# b = buses_and_offsets
result = reduce(get_recurring_pattern, buses_and_offsets)

print(result[0] - result[1])

toc = perf_counter()
print(toc - tic)


# PART TWO BRUTE FORCE c 0.129 secs on example
# tic = perf_counter()
# time_offsets = [i for i, bus in enumerate(all_buses) if bus != 'x']
# buses_and_offsets = list(zip(named_buses, time_offsets))

# departure_count_of_first_bus = 1
# while True:
#     test_time = departure_count_of_first_bus * buses_and_offsets[0][0]
#     if all((test_time + tup[1]) % tup[0] == 0 for tup in buses_and_offsets):
#         break
#     departure_count_of_first_bus += 1
    
# print(test_time)

# toc = perf_counter()
# print(toc - tic)

# # PART TWO IMPROVED BRUTE FORCE c 0.019 secs on example
# tic = perf_counter()
# rarest_bus = max(named_buses)
# rarest_bus_index = all_buses.index(str(rarest_bus))
# time_offsets = [rarest_bus_index - i for i, bus in enumerate(all_buses) if bus != 'x']
# buses_and_offsets = list(zip(named_buses, time_offsets))

# departure_count_of_rarest_bus = 1
# tic_count = 1

# while True:
#     test_time = departure_count_of_rarest_bus * rarest_bus
#     if all((test_time - tup[1]) % tup[0] == 0 for tup in buses_and_offsets):
#         break
#     departure_count_of_rarest_bus += 1
    
# print(test_time - buses_and_offsets[0][1])

# toc = perf_counter()
# print(toc - tic)
