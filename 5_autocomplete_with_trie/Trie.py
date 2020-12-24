# Decide to user Dict instead of object, because Dict is printable

def initTrieNode():
    data = {}
    data['word_end'] = False
    return data


def findSuffixTrieNode(node):
    answer = []

    def recursiveTraverse(node, word):
        if node['word_end']:
            answer.append(word)

        for k, next_node in node.items():
            if(k == 'word_end'):
                continue
            next_word = word + k
            recursiveTraverse(next_node, next_word)

    recursiveTraverse(node, '')
    return answer


def insertTrieNode(node, char):
    node[char] = initTrieNode()


class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root = {}

    def insert(self, word):
        # Add a word to the Trie

        def recursiveAdd(node, word):
            if len(word) == 0:
                node['word_end'] = True
                return

            char = word[0]
            tail = word[1:]
            if not char in node:
                insertTrieNode(node, char)
                recursiveAdd(node[char], tail)
            else:
                next_node = node[char]
                recursiveAdd(next_node, tail)

        recursiveAdd(self.root, word)

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
