import time

puzzle_input = [1,20,11,6,12,0]

def play(start_nums, iterations):
    last_calls = {}
    said_num = None    
    for i in range(iterations):
        if i < len(start_nums):
            last_calls[said_num], said_num = i, start_nums[i]  
        elif said_num in last_calls: 
            last_calls[said_num], said_num = i, i - last_calls[said_num]
        else:
            last_calls[said_num], said_num = i, 0
    return said_num

tic = time.perf_counter()
print(play(puzzle_input, 30000000))
toc = time.perf_counter()
print("Complete in " + str(toc - tic))    