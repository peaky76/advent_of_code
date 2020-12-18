import time

file = open("puzzle_input.txt", "r")
expressions = [line.rstrip('.\n') for line in file]

def is_bracketed(sequence):
    return '(' in sequence[0] and ')' in sequence[-1] and not any(bracket in element for bracket in ['(', ')'] for element in sequence[1:-1])

def is_bracket_free(sequence):
    return not any('(' in x for x in sequence) and not any(')' in x for x in sequence)    

def evaluate(expression, precedent_op=None):
    if '(' in expression or ')' in expression:
        raise Exception("Brackets in expression being evaluated")
    if precedent_op:
        while precedent_op in expression:
            elements = expression.split(' ')
            for i in range(len(elements) - 2):
                if elements[i+1] == precedent_op:
                    new_element = str(eval(' '.join(elements[i:i+3])))
                    expression = ' '.join([*elements[:i], new_element, *elements[i+3:]])
                    break
        return eval(expression)
    else:
        elements = expression.split(' ')
        if len(elements) == 3:
            return eval(expression)
        else:
            new_element = str(eval(' '.join(elements[:3])))
            return evaluate(' '.join([new_element, *elements[3:]])) 
    
def unfold(expression, precedent_op=None):
    while '(' in expression:
        reevaluate = False
        elements = expression.split(' ')
        for i in range(len(elements) - 2):
            if '(' in elements[i]:
                for j in range(i+2, len(elements)):
                    if ')' in elements[j]:
                        if is_bracketed(elements[i:j+1]):
                            left_bracket_count = elements[i].count('(')
                            right_bracket_count = elements[j].count(')')
                            debracketed_expr = ' '.join(elements[i:j+1]).replace('(','').replace(')','')
                            new_element = '(' * (left_bracket_count - 1)
                            new_element += str(evaluate(debracketed_expr, precedent_op))
                            new_element += ')' * (right_bracket_count - 1)
                            expression = ' '.join([*elements[:i], new_element, *elements[j+1:]])
                            reevaluate = True
                            break
                if reevaluate:
                    break
    return evaluate(expression, precedent_op)
        
# PART ONE
print(sum([unfold(expression) for expression in expressions]))

# PART TWO
print(sum([unfold(expression, '+') for expression in expressions]))