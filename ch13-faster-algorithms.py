def greatest_product_of_3_numbers(numbers):
    if len(numbers) < 3: return None

    # Make it easy to find the three largest numbers by pre-sorting instead of
    # comparing any set of three numbers (which is O(N^3))
    numbers.sort()
    return numbers[-1] * numbers[-2] * numbers[-3]

def find_missing_numbers_in_range(numbers):
    numbers.sort()
    missing = []
    current = 0
    
    for i in numbers:
        # We expected a value, but the array's index value is bigger (i.e., we skipped)
        if current < i:
            # Catch up 'current' until we've got a match, making a list of what we've had to catch up on
            while current < i:
                missing.append(current)
                current += 1
        # Found what we expected, so carry on with the next increment
        else: 
            current += 1

    return missing

def find_biggest_value_N_squared(numbers):
    if len(numbers) == 0: return None

    # Compare current value to every other value for N values. Oh God, why would you ever do this?
    for left in range(len(numbers)):
        leftIsBigger = True
        for right in range(len(numbers)):
            if numbers[right] > numbers[left]: leftIsBigger = False

        if leftIsBigger: return numbers[left]

def find_biggest_value_N_log2_N(numbers):
    if len(numbers) == 0: return None
    
    # The biggest is the last value of the list when sorted
    numbers.sort()
    return numbers[-1]

def find_biggest_value_N(numbers):
    if len(numbers) == 0: return None
    
    # Assume the first value is the biggest, then walk through the list
    # noting when we found a bigger one.
    biggest = numbers[0]
    for i in numbers:
        if i > biggest: biggest = i

    return biggest

numbers = [50, 20, 1, 5, 3]
print(greatest_product_of_3_numbers(numbers))

missing = [9, 3, 2, 5, 1, 0, 4]
print(find_missing_numbers_in_range(missing))

numbers = [50, 20, 1, 5, 3]
print(find_biggest_value_N_squared(numbers))

numbers = [50, 20, 1, 5, 3]
print(find_biggest_value_N_log2_N(numbers))

numbers = [50, 20, 1, 5, 3]
print(find_biggest_value_N(numbers))