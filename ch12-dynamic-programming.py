def add_until_100(numbers):
    if len(numbers) == 0: return 0

    sum = numbers[0]
    for x in range(1,len(numbers)):
        if sum + numbers[x] > 100: return sum
        sum += numbers[x]

    return sum

def golumb_memoization(n, memo):
    if n == 1: return 1

    if n not in memo.keys():
        memo[n] = 1 + golumb_memoization(n - golumb_memoization(golumb_memoization(n-1, memo), memo), memo)

    return memo[n]

def count_unique_paths_memoization(rows, columns, memo):
    # Assumes start is upper left, finish is lower right.
    if rows == 1 or columns == 1: return 1
    
    lookup = "{r}.{c}".format(r = rows, c = columns)
    if lookup not in memo.keys():
        memo[lookup] = count_unique_paths_memoization(rows - 1, columns, memo) + count_unique_paths_memoization(rows, columns - 1, memo)
    
    return memo[lookup]

numbers = [1, 2, 3, 4, 5, 84, 10]
print("Sum of numbers that doesn't exceed 100")
print(numbers)
print(add_until_100(numbers))

print("golumb(10)")
print(golumb_memoization(10, {}))

print("Number of unique paths from upper-left to lower-right in 7x3 grid...")
print(count_unique_paths_memoization(3, 7, {}))