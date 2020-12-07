from bagrule import BagRule
from collections.abc import Iterable

file = open("puzzle_input.txt", "r")
bag_rules = []

for line in file:
    line = line.rstrip('.\n')

    outer_bag = line.split(' bags contain ')[0]
    inner_bags = line.split(' bags contain ')[1].split(', ')

    bag_rule = BagRule(outer_bag)
    if inner_bags != ["no other bags"]:
        for bag in inner_bags:
            color = ' '.join(bag[2:].split(' ')[:-1])
            number = int(bag[0])
            bag_rule.add_inner(color, number)

    bag_rules.append(bag_rule)
    
#PART ONE
def get_valid_outers(bag_color):
    immediate_outers = [rule.outer for rule in bag_rules if bag_color in rule.inners.keys()]
    return immediate_outers + [get_valid_outers(color) for color in immediate_outers]

def flatten(l):
    for el in l:
        if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el

print(len(set(list(flatten(get_valid_outers('shiny gold'))))))

#PART TWO
def get_internal_bag_count(bag_color):
    immediate_inners = [(k, v) for rule in bag_rules for k, v in rule.inners.items() if rule.outer == bag_color ]
    immediate_inners_count = sum([v for (k, v) in immediate_inners])
    return immediate_inners_count + sum([v * get_internal_bag_count(k) for (k, v) in immediate_inners])

print(get_internal_bag_count('shiny gold'))
