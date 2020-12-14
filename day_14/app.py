file = open("puzzle_input.txt", "r")
lines = [line for line in file]

# PREPARATION

bitmasks = []
memory_writes = []

for instruction in lines:
    if instruction[:2] == "ma":
        bitmasks.append(instruction.split(' = ')[1].rstrip('\n'))        
    else:
        slot = int(instruction.split('] = ')[0].lstrip('mem['))
        value = int(instruction.split('] = ')[1].rstrip('\n'))
        memory_writes.append((slot, value, len(bitmasks) - 1))  

# FUNCTIONS
    
def apply_bitmask(number, bitmask, version):
    bin_num = '{:0{l}b}'.format(number, l=len(str(bitmask)))
    bitpairs = zip(str(bitmask), str(bin_num))
    return ''.join([convert_bit(bitpair, version) for bitpair in bitpairs])             

def apply_floating_bits(floating_bit_num):
    alternatives = ['']
    for char in list(floating_bit_num):
        for i in range(len(alternatives)):
            if char == 'X':
                alternatives.append(alternatives[i] + '0')
                alternatives[i] += '1'
            else:
                alternatives[i] += char              
    return alternatives
    
def convert_bit(bitpair, version):
    if version == 1:
        return bitpair[1] if bitpair[0] == 'X' else bitpair[0]
    else:
        return bitpair[1] if bitpair[0] == '0' else bitpair[0]       

def get_total(memory_writes, bitmask_rule_to_apply=None):
    total = 0
    memory_slots_to_empty = set(write[0] for write in memory_writes)   
    for write in memory_writes[::-1]:
        if write[0] in memory_slots_to_empty:
            if bitmask_rule_to_apply:
                total += int(apply_bitmask(write[1], bitmasks[write[2]], bitmask_rule_to_apply), 2)     
            else:
                total += write[1]
            memory_slots_to_empty.remove(write[0]) 
    return total
        
# PART ONE        
print(get_total(memory_writes, 1))        

# # PART TWO
converted_memory_writes = []
for write in memory_writes:
    for conversion in apply_floating_bits(apply_bitmask(write[0], bitmasks[write[2]], version=2)):
        converted_memory_writes.append((int(conversion, 2), write[1], None))

print(get_total(converted_memory_writes))