import time
import resource
import sys

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quicksort(left) + [pivot] + quicksort(right)

# Get user input for array
arr = input("Enter array of numbers, separated by space: ")
arr = list(map(int, arr.split()))

# Increase recursion limit
sys.setrecursionlimit(len(arr)*2)

# Start stopwatch
start_time = time.time()

# Call quicksort function
arr = quicksort(arr)

# Stop stopwatch
end_time = time.time()
elapsed_time = end_time - start_time

# Get maximum memory usage
max_memory_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024 / 1024 # in MB

# Print sorted array, elapsed time, and max memory usage
print("Sorted array: ", arr)
print("Elapsed time: ", elapsed_time, "Seconds")
print("Max memory usage: ", max_memory_usage, "MB")
