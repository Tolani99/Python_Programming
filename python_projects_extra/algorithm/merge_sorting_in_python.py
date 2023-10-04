def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temporary arrays
    L = [0] * n1
    R = [0] * n2

    # copy data to temporary arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temporary arrays back into arr[1..r]
    i = 0 # Initialize the first index of the subarray
    j = 0 # Initizlize the second index of the subarray
    k = l # Initialize the index of the merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# l is for left index and r is right index of the sub-array of arr to be sorted

def mergeSort(arr, l, r):
    if l < r:

        # same as (l+r)//2
        m = l + (r - l)//2

        # sort the first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

# Drive code to test above
print("Input the array you want to test: ")

# Accepting input as a string
input_string = input("Enter a list of integers separated by space: ")

# Splitting the input string into individual elements
input_list = input_string.split()

# Converting each element to an integer
try:
    # Using list comprehension to convert elements to integers
    arr = [int(num) for num in input_list]
    print("List of integers:", arr)
except ValueError:
    print("Invalid input. Please enter integers separated by space.")

n = len(arr)
print("Given array is: ")
for i in range(n):
    print("%d" % arr[i], end = " ")

mergeSort(arr, 0, n-1)
print("\n\nSorted array is")
for i in range(n):
    print("%d" % arr[i], end = " ")
print("\n")

