from functools import reduce
from time import perf_counter

file = open("puzzle_input.txt", "r")
lines = [line for line in file]

curr_time = int(lines[0].rstrip('\n'))
all_buses = [bus for bus in lines[1].rstrip('\n').split(',')]
named_buses = [int(bus) for bus in all_buses if bus != 'x']

def next_arrival_time(bus, curr_time):
    return (curr_time // bus + 1) * buss

def get_recurring_pattern(bus_a, bus_b):
    spacing = bus_a[0] * bus_b[0]
    max_bus, min_bus = sorted([bus_a, bus_b], reverse=True)
      
    multiple = 1
    while (max_bus[0] * multiple - max_bus[1] + min_bus[1]) % min_bus[0] != 0:
        multiple += 1
    
    first_occurrence = max_bus[0] * multiple - max_bus[1]
    
    return (spacing, spacing - first_occurrence) 
          
# PART ONE
next_arrival_times = dict([(bus, next_arrival_time(bus, curr_time)) for bus in named_buses])
soonest_bus = min(next_arrival_times, key=next_arrival_times.get)
print(soonest_bus * (next_arrival_times[soonest_bus] - curr_time))

# PART TWO
time_offsets = [i for i, bus in enumerate(all_buses) if bus != 'x']
buses_and_offsets = sorted(list(zip(named_buses, time_offsets)), reverse=True)
result = reduce(get_recurring_pattern, buses_and_offsets)
print(result[0] - result[1])