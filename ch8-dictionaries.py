import string

# Returns an array with elements that are in both first_arr and second_arr.
# Initial attempt.
def array_intersection_v1(first_arr, second_arr):
    intersection = {}

    # Insertion is O(N)
    for i in first_arr:
        if i in intersection:
            intersection[i] += 1
        else:
            intersection[i] = 1

    # Insertion is O(M)
    for i in second_arr:
        if i in intersection:
            intersection[i] += 1
        else:
            intersection[i] = 1

    # Enumeration is O(N+M)
    to_return = []
    for x in intersection.keys():
        if intersection[x] > 1:
            to_return.append(x)
    return to_return

# Returns an array with elements that are in both first_arr and second_arr.
# (Book's version)
def array_intersection_v2(first_arr, second_arr):
    bookkeeping = {}

    # Insertion is O(N)
    for i in first_arr:
        bookkeeping[i] = True

    # Enumeration is O(M)
    to_return = []
    for i in second_arr:
        if i in bookkeeping:
            to_return.append(i)

    return to_return

def find_first_duplicate(values):
    string_freq = {}

    # Best case is O(2) where the second element is a dupe if the first
    # Worst case is O(N) where there are no dupes.
    for i in values:
        if i in string_freq:
            return i
        else:
            string_freq[i] = True

    return None

def find_missing_letters(phrase):
    
    # O(N) to build up the bookkeeping
    found_chars = {}
    for c in phrase:
        found_chars[c] = True

    # O(26) --> O(1) to check each lowercase letter
    missing_letters = []
    for c in string.ascii_lowercase:
        if c not in found_chars:
            missing_letters.append(c)

    return missing_letters

def find_nonduplicated_letters(phrase):
    
    # O(N) to build up the bookkeeping
    chars_freq = {}
    for c in phrase:
        if c in chars_freq:
            chars_freq[c] += 1
        else:
            chars_freq[c] = 1

    # Worst-case enumeration is O(N)
    to_return = []
    for x in chars_freq.keys():
        if chars_freq[x] == 1:
            to_return.append(x)
    return to_return



# Array intersection example
first_arr = [1, 2, 3, 4, 5]
second_arr = [0, 2, 4, 6, 8]
print(array_intersection_v1(first_arr, second_arr))
print(array_intersection_v2(first_arr, second_arr))

# String duplicate example
values_with_dupe = ["cat", "dog", "bear", "dog", "snake"]
print(find_first_duplicate(values_with_dupe))

# Missing letters example
print(find_missing_letters("The quick brown box jumps over the lazy dog"))

# Finding non-duplicated letters
print(find_nonduplicated_letters("minimum"))