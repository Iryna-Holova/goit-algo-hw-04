"""
Merge Sort Algorithm
"""


def merge_sort(arr: list) -> list:
    """
    Merge Sort Algorithm.

    Args:
        arr (list): List of elements to be sorted.

    Returns:
        list: Sorted list.
    """
    if len(arr) <= 1:  # Base case
        return arr

    mid = len(arr) // 2  # Find the middle index
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left: list, right: list) -> list:
    """
    Merge two sorted lists into a single sorted list.

    Args:
        left (list): Left half of the list.
        right (list): Right half of the list.

    Returns:
        list: Merged list.
    """
    merged = []
    left_index = 0
    right_index = 0

    # Compare and merge elements from both halves
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Append remaining elements if any
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

# Time complexity: O(n log(n))
# Space complexity: O(n)
