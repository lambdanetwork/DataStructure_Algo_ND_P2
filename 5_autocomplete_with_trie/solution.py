from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
from Trie import Trie, findSuffixTrieNode


def f(prefix):
    if prefix != '':
        (prefix, prefixNode) = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(findSuffixTrieNode(prefixNode)))
        else:
            print(prefix + " not found")
    else:
        print('')


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

f('fu')
