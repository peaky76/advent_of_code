import time

puzzle_input = [1,20,11,6,12,0]

def play(start_nums, iterations):
    last_calls = {}
    last_num = said_num = None
    for i in range(iterations):
        if i < len(start_nums):
            said_num = start_nums[i]
        elif last_num in last_calls: 
            said_num = i - last_calls[said_num]
        else:
            said_num = 0
        if last_num != None:
            last_calls[last_num] = i
        last_num = said_num
    return said_num

tic = time.perf_counter()
print(play([0,3,6], 30000000))
toc = time.perf_counter()
print("Complete in " + str(toc - tic))    