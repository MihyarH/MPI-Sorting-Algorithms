import time
import resource


def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # Return the sorted array
    return arr


# Ask the user to input the array to be sorted
arr = list(map(int, input("Enter the array to be sorted, separated by spaces: ").split()))

# Start the stopwatch
start_time = time.time()

# Get the current memory usage
start_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

# Sort the array using bubble sort
sorted_arr = bubble_sort(arr)

# Stop the stopwatch
end_time = time.time()

# Get the maximum memory usage during sorting
end_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

# Print the sorted array and timing/memory information
print("Sorted array is:", sorted_arr)
print("Time taken:", end_time - start_time, "Seconds")
print("Maximum memory usage:", end_mem / 1024 / 1024, "MB")
