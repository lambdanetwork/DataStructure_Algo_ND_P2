### Problem
## HTTPRouter using a Trie

For this exercise we are going to implement an HTTPRouter like you would find in a typical web server using the Trie data structure we learned previously.

There are many different implementations of HTTP Routers such as regular expressions or simple string matching, but the Trie is an excellent and very efficient data structure for this purpose.

The purpose of an HTTP Router is to take a URL path like "/", "/about", or "/blog/2019-01-15/my-awesome-blog-post" and figure out what content to return. In a dynamic web server, the content will often come from a block of code called a handler.

### Strategy
- Router Trie is variaton of Trie
- The difference is:
- insert path:
    * we will split the word by `/` and remove the trailing `/`
    * Each word becomes path and added to `self.root`
    * each Node has key `handler`, 
    * when we finish adding the last word, we will record the pointer to handler-function in key `handler`
- search path:
    * we will split the word by `/` and remove the trailing `/`
    * Traverse each child of node
    * if the last node has handler, return it, else return false