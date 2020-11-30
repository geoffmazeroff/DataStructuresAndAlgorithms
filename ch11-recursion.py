def count_chars_recursive(strings):
    if len(strings) == 1:
        #print("String: {thisstr} = {numchars} chars".format(thisstr = strings[0], numchars = len(strings[0])))
        return len(strings[0])

    #print("This string is {thisstr} with {numchars} chars; plus {others}".format(thisstr = strings[0], numchars = len(strings[0]), others = strings[1:]))
    return len(strings[0]) + count_chars_recursive(strings[1:])

def find_even_numbers_recurive(values):
    if not values: return []
    
    # I tried "list comprehensions" to solve returning nonsense results with nested
    # arrays like [2, [4, []]] and got nowhere. I'm not pleased with this approach of
    # temporary arrays to prevent nesting dolls, but (1) it works, (2) the book author
    # provided no solution in Python.

    toreturn = []
    if values[0] % 2 == 0:
        print("First value ({val}) in the list was even".format(val = values[0]))
        print("Now finding other evens in {others}".format(others = values[1:]))
        toreturn.append(values[0])
        othervals = find_even_numbers_recurive(values[1:])
        for v in othervals:
            toreturn.append(v)
        return toreturn
    else:
        print("First value ({val}) in the list was odd".format(val = values[0]))
        print("Now finding other evens in {others}".format(others = values[1:]))
        othervals = find_even_numbers_recurive(values[1:])
        for v in othervals:
            toreturn.append(v)
        return toreturn

def find_triangular_sum_recursive(val):
    if val == 1: return 1
    return val + find_triangular_sum_recursive(val - 1)

def find_x_recursive(targetstr, index):
    if index == len(targetstr): return -1      # Reached the end of the string
    if targetstr[index] == 'x': return index   # Found it!
    return find_x_recursive(targetstr, index+1)

def count_unique_paths_recursive(rows, columns):
    # Assumes start is upper left, finish is lower right.
    if rows == 1 or columns == 1: return 1
    return count_unique_paths_recursive(rows - 1, columns) + count_unique_paths_recursive(rows, columns - 1)

print("Count of chars in [ab, c, def, ghij]...")
print(count_chars_recursive(["ab", "c", "def", "ghij"]))

print("Even numbers from [1, 2, 3, 4, 5]")
print(find_even_numbers_recurive([1, 2, 3, 4, 5]))

print ("Triangular sum of 7...")
print(find_triangular_sum_recursive(7))

print("Finding x in abcdefghijklmnopqrstuvwxyz...")
print(find_x_recursive("abcdefghijklmnopqrstuvwxyz", 0))

print("Number of unique paths from upper-left to lower-right in 7x3 grid...")
print(count_unique_paths_recursive(3, 7))