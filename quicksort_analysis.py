# quicksort_analysis.py
# Comparison of Deterministic Quicksort and Randomized Quicksort

import random
import time
import sys

# Increase recursion limit for handling larger input sizes
sys.setrecursionlimit(20000)

def deterministic_partition(array, start, end):
    """
    Partition the array using the first element as the pivot (deterministic approach).
    Elements smaller than or equal to the pivot are placed on the left, 
    while elements greater are placed on the right.
    """
    pivot_element = array[start]  # Use the first element as the pivot
    partition_index = start
    for current_index in range(start + 1, end + 1):
        if array[current_index] <= pivot_element:
            partition_index += 1
            array[partition_index], array[current_index] = array[current_index], array[partition_index]
    array[start], array[partition_index] = array[partition_index], array[start]
    return partition_index

def deterministic_quicksort(array, start, end):
    """
    Implements Deterministic Quicksort using the first element as the pivot.
    """
    if start < end:
        pivot_location = deterministic_partition(array, start, end)
        deterministic_quicksort(array, start, pivot_location - 1)
        deterministic_quicksort(array, pivot_location + 1, end)

def randomized_partition(array, start, end):
    """
    Partition the array using a randomly selected pivot.
    This typically results in more balanced partitions on average.
    """
    random_pivot = random.randint(start, end)
    array[random_pivot], array[start] = array[start], array[random_pivot]  # Swap with the first element
    return deterministic_partition(array, start, end)

def randomized_quicksort(array, start, end):
    """
    Implements Randomized Quicksort using a random pivot for partitioning.
    """
    if start < end:
        pivot_location = randomized_partition(array, start, end)
        randomized_quicksort(array, start, pivot_location - 1)
        randomized_quicksort(array, pivot_location + 1, end)

def generate_test_array(size, pattern="random"):
    """
    Generate test arrays with different patterns:
    - "sorted": Array is in ascending order.
    - "reversed": Array is in descending order.
    - "repeated": Array contains many repeated values.
    - "random": Array elements are randomized.
    """
    if pattern == "sorted":
        return list(range(size))
    elif pattern == "reversed":
        return list(range(size, 0, -1))
    elif pattern == "repeated":
        return [random.randint(0, size // 10) for _ in range(size)]
    else:
        return [random.randint(0, size) for _ in range(size)]

def measure_execution_time(sort_function, array):
    """
    Measure the execution time of a sorting function.
    """
    start_time = time.time()
    sort_function(array, 0, len(array) - 1)
    return time.time() - start_time

def display_results(comparison_data, sizes, patterns):
    """
    Display the performance results of Deterministic and Randomized Quicksort.
    """
    print(f"{'Input Size':<12}{'Pattern':<15}{'Deterministic (s)':<20}{'Randomized (s)':<20}")
    print("-" * 70)
    for pattern in patterns:
        for size, det_time, rand_time in zip(sizes, comparison_data["Deterministic"][pattern], comparison_data["Randomized"][pattern]):
            print(f"{size:<12}{pattern:<15}{det_time:<20.6f}{rand_time:<20.6f}")

def compare_quicksort_variants():
    """
    Compare the performance of Deterministic and Randomized Quicksort 
    on arrays with varying patterns and sizes.
    """
    input_sizes = [100, 500, 1000, 5000, 10000]
    array_patterns = ["random", "sorted", "reversed", "repeated"]
    performance_data = {"Deterministic": {}, "Randomized": {}}

    for pattern in array_patterns:
        performance_data["Deterministic"][pattern] = []
        performance_data["Randomized"][pattern] = []

        for size in input_sizes:
            test_array = generate_test_array(size, pattern=pattern)
            performance_data["Deterministic"][pattern].append(measure_execution_time(deterministic_quicksort, test_array.copy()))
            performance_data["Randomized"][pattern].append(measure_execution_time(randomized_quicksort, test_array.copy()))

    display_results(performance_data, input_sizes, array_patterns)

compare_quicksort_variants()
