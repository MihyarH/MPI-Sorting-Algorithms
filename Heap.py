import time
import psutil
import random

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# Take input from the user
n = int(input("Enter the number of elements: "))
minimum = int(input("Enter the minimum value of elements: "))
maximum = int(input("Enter the maximum value of elements: "))

# Generate random elements within the specified range
arr = [random.randint(minimum, maximum) for _ in range(n)]

start_time = time.time()
start_memory = psutil.Process().memory_info().rss

heap_sort(arr)

end_time = time.time()
end_memory = psutil.Process().memory_info().rss

execution_time = end_time - start_time
memory_usage = (end_memory - start_memory) / 1024 / 1024

print("Sorted array:", arr)
print("Execution Time:", execution_time, "Seconds")
print("Maximum Memory Usage:", round(memory_usage, 2), "MB")
