# Linear Search & Binary Search Algorithms

A Python implementation of **Linear Search** and **Binary Search** with
user input support and built-in execution/runtime measurement.

## What are these algorithms?

### Linear Search
Checks every element of a list **one at a time, in order**, until it
finds the target value (or reaches the end of the list). It works on
**any list**, sorted or unsorted.

### Binary Search
Repeatedly splits a **sorted** list in half, comparing the target to
the middle element:
- If the middle element equals the target → found.
- If the target is smaller → search the left half.
- If the target is larger → search the right half.

This "divide and conquer" approach eliminates half of the remaining
elements at every step, making it much faster than linear search on
large sorted lists. **Binary search only works on sorted data.**

## Features

- `linear_search(arr, target)` — sequential search, works on any list
- `binary_search(arr, target)` — fast search on a sorted list (iterative)
- Takes **user input** from the terminal (space-separated numbers + a target)
- Automatically sorts a copy of the list for binary search
- Prints the **run time** of each algorithm using `time.perf_counter()`
- Prints the **theoretical time complexity** of each algorithm

## Files

| File                     | Description                                   |
|---------------------------|------------------------------------------------|
| `search_algorithms.py`   | Linear search, binary search, demo, and timing |
| `README.md`              | This documentation file                        |

## How to Run

```bash
python3 search_algorithms.py
```

You will be prompted for a list of numbers and a target value:

```
Enter numbers separated by spaces (e.g. 5 3 8 1 9): 9 3 7 1 8 2 5
Enter the number you want to search for: 7
```

### Example Output

```
Original list:        [9, 3, 7, 1, 8, 2, 5]
Sorted list (for binary search): [1, 2, 3, 5, 7, 8, 9]

===== Search Results =====
Linear Search: found 7 at index 2 (original list)
Binary Search: found 7 at index 4 (sorted list)

===== Execution Time Report =====
Linear Search run time (n=7, O(n)):      0.00000285 seconds
Binary Search run time (n=7, O(log n)):  0.00004801 seconds

Theoretical Time Complexity:
  Linear Search : O(n)      | Best: O(1)  | Space: O(1)
  Binary Search : O(log n)  | Best: O(1)  | Space: O(1) iterative
  Note: Binary Search requires a sorted list; sorting itself costs O(n log n).
```

> **Note:** For very small lists, binary search can sometimes *appear*
> slower than linear search in the timing report. This is normal — the
> fixed overhead of computing `mid`, `low`, and `high` on each loop can
> outweigh the benefit of halving the search space when `n` is small.
> Binary search's advantage becomes clear as `n` grows large.

## Time & Space Complexity

| Algorithm      | Best Case | Average / Worst Case | Space Complexity | Requires Sorted Input? |
|-----------------|:---------:|:---------------------:|:-----------------:|:------------------------:|
| Linear Search   | `O(1)`    | `O(n)`                | `O(1)`             | No                      |
| Binary Search   | `O(1)`    | `O(log n)`             | `O(1)` iterative / `O(log n)` recursive | Yes |

### Why is Linear Search `O(n)`?

In the worst case (target is the last element, or not present at all),
every one of the `n` elements must be checked, so the work grows
linearly with the size of the input.

### Why is Binary Search `O(log n)`?

Each comparison eliminates **half** of the remaining search space.
Starting from `n` elements, after `k` steps only `n / 2^k` elements
remain. The search ends when `n / 2^k = 1`, which gives
`k = log2(n)` steps — hence `O(log n)`.

### Important Trade-off

Binary search is only faster **if the data is already sorted**, or if
it will be searched many times (so the one-time sorting cost of
`O(n log n)` is worth paying). If you need to search an unsorted list
only once, linear search is often simpler and just as practical.

## Runtime Notes

- Run times are measured using `time.perf_counter()`, Python's
  recommended high-resolution timer for benchmarking short operations.
- Actual timing results depend on:
  - The number of elements entered (`n`)
  - Where the target is located in the list
  - The machine and Python interpreter running the script
- For small inputs, both algorithms run in microseconds and timing
  differences may not clearly reflect Big-O behavior — this becomes
  more visible as `n` increases (try lists of thousands of numbers).

## Requirements

- Python 3.6+
- No external dependencies (uses only the built-in `time` module)
