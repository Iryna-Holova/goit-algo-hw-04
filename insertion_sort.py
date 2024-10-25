"""
Insertion Sort Algorithm
"""


def insertion_sort(lst: list) -> list:
    """
    Insertion Sort Algorithm.

    Args:
        arr (list): List of elements to be sorted.

    Returns:
        list: Sorted list.
    """
    for i in range(1, len(lst)):  # Start from the second element
        key = lst[i]  # Store the current element
        j = i - 1  # Start from the previous element

        # While the current element is less than the previous element:
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]  # Move the previous element to the right
            j -= 1  # Move to the previous element
        lst[j + 1] = key  # Insert the current element to the correct position
    return lst  # Return the sorted list

# Time complexity: O(n^2)
# Space complexity: O(1)
