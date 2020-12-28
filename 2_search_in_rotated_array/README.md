## Search in a Rotated Sorted Array

### How to run
```
  python3 solution.py
```

### Problem
You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).

Example:

Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

### Solution Statement
- find number in array with Time Complexity of O(log n)

### Strategy
- We will use binary search, with slight variation, that is we must move the lower_bound by 1 index
- This is because the array is almost sorted, 
- so by moving +1 index when we divide the array, it should search in an sorted subarray

### Analysis
- Time Complexity **O(log(n))**
- Space Complexity **O(1)**