## Find Square root
- This is a variation of binary search: 
  * we will test the square(middle value) of range
  * we will have low = 0, and highest as the number to search
  * check if square of middle of (low and high) is the answer
  * if square of current middle is higher, search middle of (low , middle)
  * if square of current middle is lower, search middle of (middle , highest)
  * if middle is the same as low or high bound. This is the answer

  
- Time Complexity **O(logN)**
- Space Complexity **O(1)**