# Sorting Algorithms Comparison and Merging Sorted Lists

This repository contains Python scripts for two tasks:

1. **Comparing Sorting Algorithms** (Merge Sort, Insertion Sort, Timsort).
2. **Merging k Sorted Lists** using a divide-and-conquer approach.

## Table of Contents

- [Project Overview](#project-overview)
- [Task 1: Sorting Algorithms Comparison](#task-1-sorting-algorithms-comparison)
  - [Overview](#overview)
  - [How It Works](#how-it-works)
  - [Results](#results)
  - [Conclusion](#conclusion)
- [Task 2: Merging k Sorted Lists](#task-2-merging-k-sorted-lists)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Project Overview

This repository is focused on exploring and comparing different sorting algorithms and solving a classic problem of merging multiple sorted lists into one sorted list. The main objectives include:

1. Empirical comparison of Merge Sort, Insertion Sort, and Python's built-in Timsort.
2. Implementation of an efficient algorithm to merge multiple sorted lists.

## Task 1: Sorting Algorithms Comparison

### Overview

This task compares the performance of three sorting algorithms:

- **Merge Sort**: A divide-and-conquer algorithm with a time complexity of O(n log n).
- **Insertion Sort**: A simple sorting algorithm with a time complexity of O(n^2).
- **Timsort**: A hybrid sorting algorithm (used by Python's built-in `sorted()` and `list.sort()` methods) that combines Merge Sort and Insertion Sort.

### How It Works

The script:

1. Sorts various input lists using all three algorithms.
2. Measures the time taken by each algorithm using Python's `timeit` module.
3. Tests the algorithms on different data sets, including:
   - Randomly generated lists of integers.
   - Randomly generated lists of strings.

### Results

The time measurements were recorded for each algorithm on different data sets. The results are presented in the table below:

```bash
Size       Type       Merge Sort      Insertion Sort  Timsort
=================================================================
100        numbers    0.000153        0.000171        0.000009
100        strings    0.000171        0.000201        0.000010
1000       numbers    0.001894        0.022527        0.000102
1000       strings    0.002494        0.025332        0.000179
5000       numbers    0.015169        0.610683        0.000736
5000       strings    0.013103        0.703195        0.000893
```

### Conclusion

- **Timsort** is significantly faster than the other algorithms, due to its use of insertion sort for small runs and merge sort for larger partitions.
- **Merge Sort** performs consistently well across different input types, as expected for an O(n log n) algorithm, but it is generally slower than Timsort due to the additional overhead.
- **Insertion Sort** is much slower than the other algorithms for larger lists, as it has a time complexity of O(n^2).

These results demonstrate that Timsort's hybrid approach makes it an efficient default choice for Python's built-in sorting methods, as it balances the advantages of both merge and insertion sort.

## Task 2: Merging k Sorted Lists

### Overview

This task involves merging `k` sorted lists into one sorted list using a divide-and-conquer approach, which is similar to the merging step of the merge sort algorithm.

### How It Works

1. The `merge_k_lists` function merges pairs of sorted lists until only one sorted list remains.
2. The function uses a `merge` function of Merge sort algorithm to merge two sorted lists at each step.
3. The approach ensures efficient merging with a time complexity of O(N log k), where `N` is the total number of elements and `k` is the number of lists.

Example usage:

```python
example_lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(example_lists)
print("Merged list:", merged_list)
# Output: Merged list: [1, 1, 2, 3, 4, 4, 5, 6]
```

## Installation

To run the code in this repository, follow these steps:

```bash
git clone https://github.com/Iryna-Holova/goit-algo-hw-04.git
cd goit-algo-hw-04
```

## Usage

To run the sorting comparison script:

```bash
python sorting_compare.py
```

To run the script for merging sorted lists:

```bash
python merge_lists.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
