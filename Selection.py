import time
import resource

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Function to get memory usage
def get_memory_usage():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024 * 1024)  # Convert to MB

# Get elements from the user
elements = input("Enter the elements to be sorted (separated by spaces): ").split()
array = [int(element) for element in elements]

start_time = time.time()

# Get initial memory usage
initial_memory = get_memory_usage()

selection_sort(array)

# Calculate the elapsed time
elapsed_time = time.time() - start_time

# Get maximum memory usage during sorting
max_memory_usage = get_memory_usage() - initial_memory

print("Sorted array:", array)
print("Elapsed time:", elapsed_time, "Seconds")
print("Maximum memory usage:", max_memory_usage, "MB")
