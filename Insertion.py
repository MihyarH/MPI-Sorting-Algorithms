import time
import psutil
import resource
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Ask user for array input
arr = input("Enter the elements of the array separated by spaces: ").split()
arr = [int(x) for x in arr]

# Start stopwatch and memory tracker
start_time = time.time()
start_memory = psutil.Process().memory_info().rss

# Perform insertion sort on the array
insertion_sort(arr)

# Stop stopwatch and memory tracker
end_time = time.time()
end_memory = psutil.Process().memory_info().rss

end_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

# Print the sorted array, time taken, and maximum memory used
print("Sorted array:", arr)
print("Time taken: %.6f Seconds" % (end_time - start_time))
print("Maximum memory usage: ",end_mem / 1024 / 1024, "MB" )
