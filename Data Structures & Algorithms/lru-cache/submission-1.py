class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = self.prev = None
class LRUCache:
    # Use double linked list, and a hash table for key 
    #Insertion, deletion: O(1)

    def __init__(self, capacity: int):
        # Store the nodes
        self.cache = {}
        self.cap = capacity
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
    
    def insert(self, node: Node):
        # self.right.prev is left
        prev, next = self.right.prev, self.right
        # set left.next and right.prev to node
        prev.next = next.prev = node
        # set node's next, prev
        node.next, node.prev = next, prev

    
    def remove(self, node: Node):
        # Change the pointers so that this node's next become this node's prev
        # Next node's prev = this node's prev
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        
    # Get operation, 
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

