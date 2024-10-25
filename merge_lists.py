"""
Merge K Sorted Lists
"""

from merge_sort import merge


def merge_k_lists(lists: list) -> list:
    """
    Merge a list of sorted lists into one sorted list.

    Args:
        lists (list): List of sorted lists to be merged.

    Returns:
        list: Merged sorted list.
    """
    while len(lists) > 1:
        merged_lists = []

        # Merge pairs of lists
        for i in range(0, len(lists), 2):
            if i + 1 >= len(lists):
                # If there is only one list left, add it to the merged lists
                merged_lists.append(lists[i])
                break

            # Merge the two lists and add the result to the merged lists
            merged_lists.append(merge(lists[i], lists[i + 1]))

        # Replace the original lists with the merged lists
        lists = merged_lists

    return lists[0]


example_lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(example_lists)
print("Merged list:", merged_list)
