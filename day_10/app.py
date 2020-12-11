import math
import time

file = open("puzzle_input.txt", "r")
adapters = []

for line in file:
    line = line.rstrip('.\n')
    adapters.append(int(line))

adapters.append(0) # Add socket
adapters.append(max(adapters) + 3) # Add device
adapters = sorted(adapters)

# PART ONE
diffs = [adapters[i] - adapters[i-1] for i in range(1, len(adapters))]    
print(diffs.count(1) * diffs.count(3))

# PART TWO
def suitable_adapters(curr_adapter):
    return [adapter for adapter in adapters if 1 <= adapter - curr_adapter <= 3]

def get_path_count():

    cache = {}
    cache[adapters[-1]] = 1
     
    def _get_next_adapter_path_count(curr_adapter):
        if curr_adapter in cache:
            return cache[curr_adapter]

        count = 0
        for adapter in suitable_adapters(curr_adapter):
            count += _get_next_adapter_path_count(adapter)

        cache[curr_adapter] = count
        return count
    
    return _get_next_adapter_path_count(0)
             
adapter_graph = {}
for adapter in adapters:
    adapter_graph.update({adapter: suitable_adapters(adapter)})

print(get_path_count())
