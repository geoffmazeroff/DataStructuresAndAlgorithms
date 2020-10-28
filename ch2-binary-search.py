# Performs a binary search of the pre-sorted list 'array' in an attempt
# to find 'search_value'. If the search value isn't in the list, returns
# 'None'.
#
# Note: Prints the loop counter to the console.
def binary_search(array, search_value):

    lower_bound = 0
    upper_bound = len(array)-1
    loop_count = 1

    while lower_bound <= upper_bound:
        
        print("[Loop count: " + str(loop_count) + "]")
        midpoint = (upper_bound + lower_bound) // 2   # The // operator is for integer division
        value_at_midpoint = array[midpoint]

        if search_value == value_at_midpoint:
            return midpoint
        elif search_value < value_at_midpoint:
            upper_bound = midpoint - 1
        elif search_value > value_at_midpoint:
            lower_bound = midpoint + 1

        loop_count += 1

    return None

array = [3, 17, 75, 80, 202]
search_value = 75

print("Index of " + str(search_value) + ": " + str(binary_search(array, search_value)))