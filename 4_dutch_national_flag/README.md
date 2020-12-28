## Dutch National Flag Problem

### How to run
```
  python3 solution.py
```
### Problem

Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be an O(n) solution but it will not count as single traversal.

Here is some boilerplate code and test cases to start with:

### Solution Statement
- Sort array in single traversal

### Strategy
- Simple rule:
  * insert 0 from beginning of array
  * insert 2 from end of array
  * insert 1 in middle of array
  
### Analysis
- Time Complexity **O(n)**
- Space Complexity **O(1)**