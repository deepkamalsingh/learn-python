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

grouped = itertools.chain([1,2,3], [4,5,6], [7,8,9])
grouped2 = itertools.chain.from_iterable([[1,2,3], [4,5,6], [7,8,9]]) # concatenate lists.

# itertools.groupby only group the consecutive same elements.
# to do the grouping you can do `frozenset(dict(Counter(s)).items())`
```

## slicing and string manipulation
- how slicing `sequence[start:stop:step]` works
    - Mental model: think of indices as pointing to the boundaries (the "slots") between characters.
    -   ```
           P   Y   T   H   O   N
         |   |   |   |   |   |   |
         0   1   2   3   4   5   6   (Positive)
        -6  -5  -4  -3  -2  -1       (Negative)
         ^           ^
        Start       Stop

        s[:-3] = s[0:-3:1] = so start at 0 and stop at -3 hence the output is "PYT"

       


        s[::-1] = s[6:0:-1] = "NOHTYP"

        s = "BENGALURU" # len(9)
           B   E   N   G   A   L   U   R   U
         |   |   |   |   |   |   |   |   |   |
         0   1   2   3   4   5   6   7   8   9     
        -9  -8  -7  -6  -5  -4  -3  -2  -1       
        s[-3:] # "URU"
        s[2:-2] # "NGALU"
        s[::-2] # "UUANB"
        s[5:2:-1] # "LAG"
        s[1:5:-1] # empty string as it is a conflict.
        s[100] # gives index error
        s[0:100] # gracefully handled and gives the complete string.
        s[100:200] # gracefully handled and gives empty string.

        ```

- ```python
    s = "abcdefghijklmnopqrst"
    print(len(s)) # 20
    # reversing the string
    print(s[::-1]) # tsrqponmlkjihgfedcba
    # slicing
    print(s[4:20:2]) # egikmoqs
    # reverse slicing
    print(s[4::-2]) # eca
    # -ve indexing
    print(s[-20]) # a
    # print(s[-21]) # IndexError: string index out of range
    # rotating the array
    print(s[5:] + s[:5]) # fghijklmnopqrstabcde
    # last 3 elements
    print(s[-3:]) # rst
    # removing last three elements
    print(s[:-3]) # abcdefghijklmnopq


    chars = ['h', 'e', 'l', 'l', 'o']
    # O(n^2)
    s1 = ""
    for c in chars:
        s1 += c
    print(s1) # 'hello'
    # O(n)
    s2 = "".join(chars) 
    print(s2) # 'hello'


    first, *middle, last = [1, 2, 3, 4, 5]
    # first = 1, middle = [2, 3, 4], last = 5
    ```

## set operations
```python
set_a = {1, 2, 3}
set_b = {3, 4, 5}

intersection = set_a & set_b  # {3}
union = set_a | set_b         # {1, 2, 3, 4, 5}
difference = set_a - set_b    # {1, 2}
```


# python builtin-methods

## any/all
- `any(iterable)` - Short-circuits on the first True.
- `all(iterable)` - Short-circuits on the first False.


## Truthiness
empty structures `([], {}, set(), "", 0, None)` are logically False


## enumerate
```python
for idx, val in enumerate(arr,start=1):
    if val == target:
        return idx
```

## zip
`zip(*iterables)` Aggregates elements from each of the iterables into tuples. It stops at the shortest iterable.
```python
for name, val in zip(names, vals):
    print(f"{name}: {val}")

matrix = [[1, 2], [3, 4], [5, 6]]
transposed = list(zip(*matrix)) # [(1, 3, 5), (2, 4, 6)]
```

## reversed
created an iterator (is memory efficient) which reverse travels the list instead of `list.reverse()` which is in-place and `arr[::-1]` which creates a new copy.

## maths
- Use `divmod(a, b)` to get `quotient`, `remainder` as it does a single division at C level.
- `sum(iterable)` highly optimized for numerical elements, to add string use `"".join(iterable)`.
- `pow(base, exp, mod=None)` alot faster than `base ** exp`.
- `a // b` does the floor division.

## sorting
- `sorted(iterable, key=None, reverse=False)` returns a iterable.

# Misc

## common foot guns:

### references
```python
a = b = c = []
a.append(1)
print(a, b, c) # [1] [1] [1]
```

## Modules imported by leetcode
```
--- Loaded Modules ---
__future__
__main__
_abc
_ast
_bisect
_bz2
_codecs
_collections
_collections_abc
_compression
_datetime
_decimal
_distutils_hack
_frozen_importlib
_frozen_importlib_external
_functools
_heapq
_imp
_io
_json
_locale
_lzma
_opcode
_operator
_random
_sha512
_signal
_sitebuiltins
_sre
_stat
_statistics
_string
_thread
_typing
_uuid
_warnings
_weakref
_weakrefset
abc
argparse
array
ast
bisect
builtins
bz2
codecs
collections
collections.abc
contextlib
copy
copyreg
dataclasses
datetime
decimal
dis
encodings
encodings.aliases
encodings.utf_8
enum
errno
fnmatch
fractions
functools
genericpath
gettext
heapq
importlib
importlib._bootstrap
importlib._bootstrap_external
importlib.machinery
inspect
io
itertools
json
json.decoder
json.encoder
json.scanner
keyword
linecache
locale
lzma
marshal
math
numbers
opcode
operator
orjson
orjson.orjson
os
os.path
platform
posix
posixpath
precompiled
precompiled.__assert__
precompiled.__deserializer__
precompiled.__serializer__
precompiled.__settings__
precompiled.__utils__
precompiled.listnode
precompiled.nestedinteger
precompiled.treenode
pwd
random
re
re._casefix
re._compiler
re._constants
re._parser
reprlib
shutil
site
sitecustomize
sortedcontainers
sortedcontainers.sorteddict
sortedcontainers.sortedlist
sortedcontainers.sortedset
stat
statistics
string
sys
textwrap
time
token
tokenize
traceback
types
typing
typing.io
typing.re
ujson
uuid
warnings
weakref
zipimport
zlib
Total modules loaded: 136
```