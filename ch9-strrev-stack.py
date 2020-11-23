def reverse_string(orig_string):
    stack = []
    for c in orig_string:
        stack.append(c)
    
    rev_string = ""
    while len(stack) > 0:
        rev_string += stack.pop()

    return rev_string

print(reverse_string("abcdef"))