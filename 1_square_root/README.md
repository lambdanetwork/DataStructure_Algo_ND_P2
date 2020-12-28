## Find Square root

### How to run
```
  python3 solution.py
```

### Problem
Finding the Square Root of an Integer

Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is O(log(n))

### Solution Statement
- To get square-root in integer with time complexity of O(log(n))

### Strategy
- This is a variation of binary search: 
  * we will test the square(middle value) of range
  * we will have low = 0, and highest as the number to search
  * check if square of middle of (low and high) is the answer
  * if square of current middle is higher, search middle of (low , middle)
  * if square of current middle is lower, search middle of (middle , highest)
  * if middle is the same as low or high bound. This is the answer

### analysis
- Time Complexity **O(logN)**
- Space Complexity **O(1)**