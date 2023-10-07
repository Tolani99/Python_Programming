"""
Problem 1.5 You are given as input an unsorted array of n distinct
numbers, where n is a power of 2. Give an algorithm that identifies the
second-largest number in the array, and that uses at most n+log2 n2
comparisons. [Hint: What information do you have left over after
computing the largest number?]
"""
def get_second_highest(a):
    hi = mid = 0
    for x in a:
        if x > hi:
            mid = hi
            hi = x
        elif x < hi and x > mid:
            lo = mid
            mid = x
    return mid

print(get_second_highest([10, 9, 5, 4, 11, 100, 120, 110]))

