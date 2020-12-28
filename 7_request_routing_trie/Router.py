# Decide to user Dict instead of object, because Dict is printable

def initTrieRouter():
    data = {}
    data['handler'] = False
    return data


def insertTrieRouter(node, path_list, handler):
    if len(path_list) == 0:  # path has added, mark the last path with handler
        node['handler'] = handler
        return

    path = path_list[0]
    tail = path_list[1:]
    if not path in node:
        node[path] = initTrieRouter()

    insertTrieRouter(node[path], tail, handler)


class Router:
    def __init__(self, root_path, not_found_handler):
        # Initialize this Trie (add a root node)
        self.root = {}
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_list = [n for n in path.split('/') if n != '']
        insertTrieRouter(self.root, path_list, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler

        # Remove trailing path
        if path[-1] == '/':
            path = path[0:-1]
        path_list = [n for n in path.split('/') if n != '']
        not_found_handler = self.not_found_handler
        
        def recursiveGetNode(node, path_list):
            if len(path_list) == 0:
                if 'handler' in node and node['handler'] != False:
                    return node['handler']
                else:
                    return not_found_handler
                
            path = path_list[0]
            tail = path_list[1:]
            if not path in node:
                return not_found_handler
            else:
                return recursiveGetNode(node[path], tail)

        found_node = recursiveGetNode(self.root, path_list)
        return found_node

    