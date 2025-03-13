from collections import OrderedDict
from typing import Any, Optional

class LRU_Cache:
    """
    A class to represent a Least Recently Used (LRU) cache.

    Attributes:
    -----------
    capacity : int
        The maximum number of items the cache can hold.
    cache : OrderedDict[int, Any]
        The ordered dictionary to store cache items.
    """

    def __init__(self, capacity: int) -> None:
        """
        Constructs all the necessary attributes for the LRU_Cache object.

        Parameters:
        -----------
        capacity : int
            The maximum number of items the cache can hold.
        """
        # Check if capacity is valid
        if capacity <= 0:
            raise ValueError("Cache capacity must be greater than 0")
            
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> Optional[Any]:
        """
        Get the value of the key if the key exists in the cache, otherwise return -1.

        Parameters:
        -----------
        key : int
            The key to be accessed in the cache.

        Returns:
        --------
        Optional[Any]
            The value associated with the key if it exists, otherwise -1.
        """
        # If key exists, move it to the end (most recently used)
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        return -1

    def set(self, key: int, value: Any) -> None:
        """
        Set or insert the value if the key is not already present. When the cache reaches 
        its capacity, it should invalidate the least recently used item before inserting 
        a new item.

        Parameters:
        -----------
        key : int
            The key to be inserted or updated in the cache.
        value : Any
            The value to be associated with the key.
        """
        # If key exists, update its value and move it to the end
        if key in self.cache:
            self.cache.pop(key)
        else:
            # If cache is at capacity, remove the least recently used item
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        
        self.cache[key] = value


if __name__ == '__main__':
    # Testing the LRU_Cache class

    # Test Case 1: Basic functionality
    our_cache = LRU_Cache(5)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    assert our_cache.get(1) == 1   # Returns 1
    assert our_cache.get(2) == 2   # Returns 2
    assert our_cache.get(9) == -1  # Returns -1 because 9 is not in the cache

    our_cache.set(5, 5)
    our_cache.set(6, 6)  # This should evict key 3
    assert our_cache.get(3) == -1  # Returns -1, 3 was evicted

    # Test Case 2: Test capacity of 1
    small_cache = LRU_Cache(1)
    small_cache.set(1, 1)
    small_cache.set(2, 2)
    assert small_cache.get(1) == -1  # Returns -1, 1 was evicted
    assert small_cache.get(2) == 2   # Returns 2

    # Test Case 3: Test invalid capacity
    try:
        invalid_cache = LRU_Cache(0)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass  # Expected behavior

    print("All test cases passed!")
