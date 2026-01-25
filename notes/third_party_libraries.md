# Python third party libraries

## sortedcontainers

Similar to C++ multiset.
```python
from sortedcontainers import SortedList

# Initialize
sl = SortedList([10, 5, 20])

# Add elements (maintains sort automatically) - O(log n)
sl.add(15) 
sl.add(5)  # Duplicates allowed
print(sl)  # Output: SortedList([5, 5, 10, 15, 20])

# Remove elements - O(log n)
sl.remove(5) # Removes first occurrence of 5
print(sl)  # Output: SortedList([5, 10, 15, 20])

# Fast lookups / indexing
print(sl[0]) # Smallest item
print(sl[-1]) # Largest item
```
