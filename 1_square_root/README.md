## Find Square root
- This is like divide and conquer: the key is try to check if middle * middle is close enough for the answer
  * we will have low = 0, and highest as the number to search
  * check if square of middle of (low and high) is the answer, or close enough
  * if square of current middle is higher, search middle of (low , middle)
  * if square of current middle is lower, search middle of (middle , highest)
  * if middle is the same as low or high bound. This is the answer

  
- Time Complexity **O(logN)**
- Space Complexity **O(1)**