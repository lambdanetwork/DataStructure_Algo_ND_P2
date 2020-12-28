## Autocomplete with Tries

### How to run
```
  # please ignore the ipynb file
  python3 solution.py

```

### Problem
**Building A Trie in Python** <br />
Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.

### Note
- I am not familiar with python notebook, and the notebook way of testing it
- So I decide to create python file and create UnitTesting
- Kindly ignore the ipynb file, The file is included in boilerplate for this project

### Strategy
- I decide to use dictionary as `TrieNode` as it's printable and easy to check when traversing recursively
- class Trie will act as an interface, just an object with method,
- The main logic is function that process TrieNode like below:
  - insert word into TrieNode:
    * break word into [head, ...tail], try to insert it to current Node
    * if len(tail) is not 0, continue the logic above
    * if len(tail) is 0, mark the node as word_end=True, This is needed because to difference word like `fun`, and `function`
  - find word in TrieNode:
    * a simple tree traversal by searching for each char of the word.
    * while traversing if we encounter key `'word_end'` we will append this to answer list
    * return the answer_list
### Analysis
- Time Complexity **O(n)** n is each character of word and depth of tree
- Space Complexity **O(m * n)** m is the length of the word and n is the number of words.