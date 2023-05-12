import time
import tracemalloc


def counting_sort(A, k):
    n = len(A)
    c = [0] * (k + 1)

    for j in range(n):
        c[A[j]] += 1

    for i in range(1, k + 1):
        c[i] += c[i - 1]

    B = [0] * n

    for j in range(n - 1, -1, -1):
        B[c[A[j]] - 1] = A[j]
        c[A[j]] -= 1

    return B


# Get user input for the array elements
arr = input("Enter the array elements separated by space: ").split()
arr = [int(num) for num in arr]

k = max(arr)

# Start memory profiling
tracemalloc.start()

# Start the stopwatch
start_time = time.time()

sorted_arr = counting_sort(arr, k)

# Stop the stopwatch
end_time = time.time()
elapsed_time = round(end_time - start_time, 4)

# Get memory usage
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics("lineno")

# Find the peak memory usage
peak_memory = max(top_stats, key=lambda stat: stat.size)

print("Sorted Array:", sorted_arr)
print("Elapsed Time:", elapsed_time, "seconds")
print("Peak Memory Usage:", peak_memory.size / (1024 * 1024), "MB")
