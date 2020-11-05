def insertion_sort(list):
    num_shifts = 0
    num_comparisons = 0

    for i in range(1,len(list)):
        temp_value = list[i]
        position = i-1

        while position >= 0:
            num_comparisons += 1
            if list[position] > temp_value:
                list[position+1] = list[position]
                position -= 1
                num_shifts += 1
            else:
                break

        list[position+1] = temp_value

    return [list, num_comparisons, num_shifts]

list_to_sort = [35, 45, 10, 65, 25, 55]   # random order (average case)
#list_to_sort = [65, 55, 45, 35, 25, 10]   # reverse order (worst case)
#list_to_sort = [10, 25, 35, 45, 55, 66]    # already ordered (best case)

print("List before sorting:")
print(list_to_sort)

print("After sorting...")
sort_results = insertion_sort(list_to_sort)
print("Comparisons: %d  ||  Shifts: %d" % (sort_results[1], sort_results[2]))
print(sort_results[0])