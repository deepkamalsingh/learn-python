# Python standard modules

## collections

### deque
```python
from collections import deque

q = deque([1, 2, 3])
q.append(4)      # Add to right (end)
q.appendleft(0)  # Add to left (start) - O(1)
q.pop()          # Remove from right
q.popleft()      # Remove from left - O(1) -> CRITICAL for BFS
```

### defaultdict
```python
from collections import defaultdict

d = defaultdict(list)
d['key'].append(1)
d['key'].append(2)
print(d['key'])
```

### counter
```python
from collections import Counter

c = Counter([1, 2, 3, 1, 2, 1])
print(c.most_common(2))
```

## heapq
```python
import heapq

# 1. Standard Min-Heap
min_heap = []
heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 1)
smallest = heapq.heappop(min_heap)  # Returns 1

# 2. Max-Heap Simulation (Negate values)
nums = [1, 5, 10]
max_heap = [-n for n in nums]
heapq.heapify(max_heap)  # O(n) linear time to build heap

largest = -heapq.heappop(max_heap)  # Returns 10 (negate again to restore)

list_a = [1, 3, 5]
list_b = [2, 4, 6]
list_c = [0, 10]

lists = [list_a, list_b, list_c]

# usage: heapq.merge(*iterables, key=None, reverse=False)
merged_iterator = heapq.merge(*lists)

```

## bisect
```python
import bisect

arr = [1, 3, 4, 4, 8]

# bisect_left: First index >= x (Lower Bound)
idx_l = bisect.bisect_left(arr, 4)  # Returns 2

# bisect_right: First index > x (Upper Bound)
idx_r = bisect.bisect_right(arr, 4) # Returns 4

# Pro Tip: Elements in range [idx_l, idx_r) are equal to x.
count = idx_r - idx_l
```

## infintiy
```python
max_val = float('inf')
min_val = float('-inf')

# Perfect for "Min/Max so far" logic
current_min = float('inf')
myInf = float('inf')
z = min(myInf, 1)
print(z, myInf, type(z), type(myInf)) # 1 inf <class 'int'> <class 'float'>
```

## division and modulus
```python
a = 10
b = 3

# Floor Division (//)
result_floor = a // b  # 3

# True Division (Normal /)
result_true = a / b    # 3.3333333333333335

# Modulus (%)
result_mod = a % b     # 1
```

## itertools
```python
import itertools

nums = [1, 2, 1, 2]

# Permutations (Order matters)
perms = list(itertools.permutations(nums, 2))

# Combinations (Order doesn't matter)
combs = list(itertools.combinations(nums, 2))
print(perms) # [(1, 2), (1, 1), (1, 2), (2, 1), (2, 1), (2, 2), (1, 1), (1, 2), (1, 2), (2, 1), (2, 2), (2, 1)]
print(combs) # [(1, 2), (1, 1), (1, 2), (2, 1), (2, 2), (1, 2)]
```

## slicing
```python
s = "asbakagd"
rev = s[::-1] # reverses the string
```

## set operations
```python
set_a = {1, 2, 3}
set_b = {3, 4, 5}

intersection = set_a & set_b  # {3}
union = set_a | set_b         # {1, 2, 3, 4, 5}
difference = set_a - set_b    # {1, 2}
```




