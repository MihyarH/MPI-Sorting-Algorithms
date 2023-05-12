import time
import random
import tracemalloc


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    result = []
    left_idx = 0
    right_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    return result


if __name__ == '__main__':
    arr = []
    n = int(input("Enter the number of elements: "))

    print("Enter the elements separated by spaces:")
    elements = input().split()
    arr = [int(x) for x in elements]

    print("Sorting started...")
    start_time = time.process_time()

    tracemalloc.start()

    sorted_arr = merge_sort(arr)

    end_time = time.process_time()

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print("Sorted array:", sorted_arr)
    print("Sorting completed in", end_time - start_time, "Seconds.")
    print("Maximum memory usage:", peak / 10 ** 6, "MB.")
