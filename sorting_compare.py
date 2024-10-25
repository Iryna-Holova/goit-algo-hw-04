"""
Compare sorting algorithms on different data sets and sizes.
"""

import timeit
import random
import string
from insertion_sort import insertion_sort
from merge_sort import merge_sort


def timsort(arr: list) -> list:
    """
    Timsort Algorithm - Python's implementation of Timsort.

    Args:
        arr (list): List of elements to be sorted.

    Returns:
        list: Sorted list.
    """
    return sorted(arr)


def generate_random_numbers(size: int) -> list:
    """
    Generate random numbers.

    Args:
        size (int): Size of the list.

    Returns:
        list: List of random numbers.
    """
    return [random.randint(0, 1000) for _ in range(size)]


def generate_random_strings(size: int, length: int = 5) -> list:
    """
    Generate random strings.

    Args:
        size (int): Size of the list.
        length (int, optional): Length of the strings. Defaults to 5.

    Returns:
        list: List of random strings.
    """
    return [
        ''.join(random.choices(string.ascii_letters, k=length))
        for _ in range(size)
    ]


def measure_time(sort_func: callable, data: list) -> float:
    """
    Measure the time of sorting.

    Args:
        sort_func (callable): Sorting function.
        data (list): List of elements to be sorted.

    Returns:
        float: Time of sorting.
    """
    start_time = timeit.default_timer()
    sort_func(data.copy())  # Copy the data to avoid modifying the original
    end_time = timeit.default_timer()
    return end_time - start_time


def compare_sorting_algorithms() -> None:
    """
    Compare sorting algorithms on different data sets and sizes.
    """
    sizes = [100, 1000, 5000]  # Different data sizes
    results = []

    for size in sizes:
        # Data generation
        num_data = generate_random_numbers(size)
        str_data = generate_random_strings(size)

        # Measure the time of sorting for numbers
        num_merge_time = measure_time(merge_sort, num_data)
        num_insertion_time = measure_time(insertion_sort, num_data)
        num_timsort_time = measure_time(timsort, num_data)

        # Measure the time of sorting for strings
        str_merge_time = measure_time(merge_sort, str_data)
        str_insertion_time = measure_time(insertion_sort, str_data)
        str_timsort_time = measure_time(timsort, str_data)

        results.append({
            'size': size,
            'type': 'numbers',
            'merge_sort': num_merge_time,
            'insertion_sort': num_insertion_time,
            'timsort': num_timsort_time
        })

        results.append({
            'size': size,
            'type': 'strings',
            'merge_sort': str_merge_time,
            'insertion_sort': str_insertion_time,
            'timsort': str_timsort_time
        })

    # Print the results
    print(f"{'Size':<10} {'Type':<10} {'Merge Sort':<15} "
          f"{'Insertion Sort':<15} {'Timsort':<15}")
    print("=" * 65)
    for result in results:
        print(
            f"{result['size']:<10} {result['type']:<10} "
            f"{result['merge_sort']:<15.6f} {result['insertion_sort']:<15.6f} "
            f"{result['timsort']:<15.6f}"
        )


if __name__ == "__main__":
    compare_sorting_algorithms()
