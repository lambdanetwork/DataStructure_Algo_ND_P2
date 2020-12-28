## Max and Min in a Unsorted Array

### How to run
```
  python3 solution.py
```
### Problem
In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

Bonus Challenge: Is it possible to find the max and min in a single traversal?

### Solution Statement
- find min and max array in single traversal

### Strategy
- To get min and max, perhaps we don't need to sort the array
- we could just traverse the array and record temporary min and max compare with each element of array
  
### Analysis
- Time Complexity **O(n)**
- Space Complexity **O(1)**