#LRU CACHE

# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
# Implement the LRUCache class:
# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.
# Example 1:
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
 
# Constraints:
# 1 <= capacity <= 3000
# 0 <= key <= 104
# 0 <= value <= 105
# At most 2 * 105 calls will be made to get and put.

#this is DOUBLY LINKED LIST + BFS question
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}   # key → Node
        
        # Dummy head & tail (to avoid edge cases)
        self.head = Node(0, 0)   # LRU side
        self.tail = Node(0, 0)   # MRU side
        
        self.head.next = self.tail
        self.tail.prev = self.head

    # ---------------- HELPER FUNCTIONS ----------------

    def _remove(self, node):
        """Remove node from linked list"""
        prev_node = node.prev
        next_node = node.next
        
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_end(self, node):
        """Add node just before tail (most recent)"""
        prev_tail = self.tail.prev
        
        prev_tail.next = node
        node.prev = prev_tail
        
        node.next = self.tail
        self.tail.prev = node

    # ---------------- MAIN FUNCTIONS ----------------

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        
        # Move node to most recent
        self._remove(node)
        self._add_to_end(node)
        
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            
            # Move to most recent
            self._remove(node)
            self._add_to_end(node)
        else:
            if len(self.cache) == self.capacity:
                # Remove LRU node
                lru = self.head.next
                self._remove(lru)
                del self.cache[lru.key]
            
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_end(new_node)

cache = LRUCache(2)
cache.put(1,1)
cache.put(2,2)
print(cache.get(1))  # 1
cache.put(3,3)
print(cache.get(2))  # -1
cache.put(4,4)
print(cache.get(1))  # -1
print(cache.get(3))  # 3
print(cache.get(4))  # 4
