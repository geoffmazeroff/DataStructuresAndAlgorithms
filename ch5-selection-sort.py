def bubble_sort(list):
    num_sweeps = 0
    num_swaps = 0
    num_comparisons = 0
    unsorted_until_index = len(list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(unsorted_until_index):
            num_comparisons += 1
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                num_swaps += 1
                sorted = False
        unsorted_until_index -= 1
        num_sweeps += 1

    return [list, num_sweeps, num_comparisons, num_swaps]

def selection_sort(list):
    num_sweeps = 0
    num_swaps = 0
    num_comparisons = 0

    for i in range(len(list)-1):
        
        lowest_value_index = i
        num_sweeps += 1

        for j in range(i,len(list)):
            num_comparisons += 1
            if list[j] < list[lowest_value_index]:
                lowest_value_index = j
        
        if lowest_value_index != i:
            list[i], list[lowest_value_index] = list[lowest_value_index], list[i]
            num_swaps += 1

    return [list, num_sweeps, num_comparisons, num_swaps]

#list_to_sort = [35, 45, 10, 65, 25, 55]   # random order (average case)
list_to_sort = [65, 55, 45, 35, 25, 10]   # reverse order (worst case)
#list_to_sort = [10, 25, 35, 45, 55, 66]    # already ordered (best case)

print("List before sorting:")
print(list_to_sort)

print("\nAfter bubble sorting...")
sort_results = bubble_sort(list_to_sort)
print("Sweeps: %d  ||  Comparisons: %d  ||  Swaps: %d" % (sort_results[1], sort_results[2], sort_results[3]))
print(sort_results[0])

#list_to_sort = [35, 45, 10, 65, 25, 55]   # random order (average case)
list_to_sort = [65, 55, 45, 35, 25, 10]   # reverse order (worst case)
#list_to_sort = [10, 25, 35, 45, 55, 66]    # already ordered (best case)

print("\nAfter selection sorting...")
sort_results = selection_sort(list_to_sort)
print("Sweeps: %d  ||  Comparisons: %d  ||  Swaps: %d" % (sort_results[1], sort_results[2], sort_results[3]))
print(sort_results[0])