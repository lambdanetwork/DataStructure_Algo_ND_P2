# Decide to user Dict instead of object, because Dict is printable

def initTrieNode():
    data = {}
    data['word_end'] = False
    return data


def findSuffixTrieNode(node):
    answer = []

    def recursiveTraverse(node, word):
        if node['word_end']:  # our search has ended, process the word constructed so far
            answer.append(word)

        for k, next_node in node.items():
            if(k == 'word_end'):  # ignore word_end, to be added as next_word
                continue
            next_word = word + k
            recursiveTraverse(next_node, next_word)

    recursiveTraverse(node, '')
    return answer


def insertTrieNode(node, word):
    if len(word) == 0:  # word has added, mark the last char as word_end = True
        node['word_end'] = True
        return

    char = word[0]
    tail = word[1:]
    if not char in node:
        # add char to currentNode, if char and Node is exists, continue traversing
        node[char] = initTrieNode()

    insertTrieNode(node[char], tail)


class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root = {}

    def insert(self, word):
        # Add a word to the Trie
        insertTrieNode(self.root, word)

    def find(self, prefix):
        def recursiveGetNode(node, word):
            if len(word) == 0:
                return node

            head = word[0]
            tail = word[1:]

            if not head in node:
                return False
            else:
                return recursiveGetNode(node[head], tail)

        found_node = recursiveGetNode(self.root, prefix)
        return (prefix, found_node)
