from ticket_rule import TicketRule
import math

file = open("puzzle_input.txt", "r")
lines = [line.rstrip('\n') for line in file]

# PREPARATION
rules = []
nearby_tickets = []
section = 0
for line in lines:
    if line == "your ticket:" or line == "nearby tickets:":
        section += 1
        continue
    if line and section == 0:
        field, bounds = line.split(': ')
        bounds = bounds.split(' or ')
        rules.append(TicketRule(field, bounds))
    if line and section == 1:
        your_ticket = [int(x) for x in line.split(',')]
    if line and section == 2:
        nearby_tickets.append([int(x) for x in line.split(',')])

# PART ONE
def get_invalid_values(ticket):
    for value in ticket:
        if not any(rule.validate_value(value) for rule in rules):
            return value
        
print(sum(get_invalid_values(ticket) for ticket in nearby_tickets if get_invalid_values(ticket) != None))

# PART TWO
def get_valid_tickets(tickets):
    return [ticket for ticket in filter(lambda x: get_invalid_values(x) == None, tickets)]
    
values_per_field = []
rules_index = {i: [] for i in range(len(rules))}

for i in range(len(rules)):
    values_per_field.append([])

for ticket in get_valid_tickets(nearby_tickets):
    i = 0
    for value in ticket:
        values_per_field[i].append(value)
        i += 1
        
i = 0
for value_list in values_per_field:
    value_list = sorted(set(value_list))
    for rule in rules:
        if all(rule.validate_value(value) for value in value_list):
            rules_index[i].append(rule.field)
    i += 1

found_keys = []    
while len(found_keys) < len(rules):
    for key, value in rules_index.items():
        if len(rules_index[key]) == 1 and key not in found_keys:
            rules_index[key] = value[0]
            print(str(value) + " is " + str(key))
            found_keys.append(key)
            for other_key in rules_index:
                if other_key != key and value[0] in rules_index[other_key]:
                    rules_index[other_key].remove(value[0])
            print(rules_index)
            break

departure_indices = []
for key, value in rules_index.items():
    if value[:9] == 'departure':
        departure_indices.append(key)
        
#1,2,5,11,15,19
        
print(math.prod(your_ticket[i] for i in departure_indices))
            
            
        
                
