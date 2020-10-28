# Returns the index of 'search_value' in the already sorted 'array'.
# If 'search_value' isn't in the array, returns 'None'
def linear_search(array, search_value):
    length = len(array)
    for i in range(length):
        if array[i] == search_value:
            return i
        elif array[i] > search_value:  # If we haven't found it yet, we won't find it.
            break
    return None

search_value = 3
array = [3,17,75,80,202]

print("Index of " + str(search_value) + ": " + str(linear_search(array, search_value)))