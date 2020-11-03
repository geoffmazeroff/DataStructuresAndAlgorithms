def has_duplicate_quadratic(list):
    num_steps = 0

    for i in range(len(list)):
        for j in range(len(list)):
            num_steps += 1
            if i != j and list[i] == list[j]:
                return [True, num_steps]

    return [False, num_steps]

def has_duplicates_linear(list):
    num_steps = 0
    existing_numbers = {}

    for i in range(len(list)):
        num_steps += 1
        if list[i] in existing_numbers:
            return [True, num_steps]
        else:
            existing_numbers[list[i]] = True
    return [False, num_steps]

list_to_check = [1, 4, 5, 2, 9]  # No duplicates
#list_to_check = [1, 5, 3, 9, 4, 4]  # One duplicate

print("The list to check...")
print(list_to_check)

print("\nQuadratic search...")
quad_results = has_duplicate_quadratic(list_to_check)
print("Has duplicates? " + str(quad_results[0]))
print("Steps to complete: %d" % (quad_results[1]))

print("\nLinear search...")
linear_results = has_duplicates_linear(list_to_check)
print("Has duplicates? " + str(linear_results[0]))
print("Steps to complete: %d" % (linear_results[1]))