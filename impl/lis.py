import bisect
from typing import Iterable
    

def lis(
    a: Iterable[int],
    retrieve: bool = False,
    consider_non_increasing: bool = False
) -> tuple[int, list[int] | None]:
    
    assert not retrieve
    assert not consider_non_increasing

    d = [float("-inf")] 
    for x in a:
        if x > d[-1]:
            d.append(x)
        else:
            e = bisect.bisect_left(d, x)
            assert e < len(d)
            if d[e] > x:
                d[e] = x 
            
    return (len(d) - 1, None)