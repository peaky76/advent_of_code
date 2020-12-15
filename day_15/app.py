import time

start_nums = [1,20,11,6,12,0]
last_call_dict = {}
last_number = None

tic = time.perf_counter()
for i in range(1, 30000001):
    if start_nums:
               said_number = start_nums[0]
               start_nums.remove(said_number)
    elif last_number in last_call_dict:
               said_number = i - last_call_dict[last_number]
    else:
               said_number = 0
    last_call_dict[last_number] = i
    last_number = said_number
toc = time.perf_counter()
    
print(said_number)
print("Complete in " + str(toc - tic))    
    
