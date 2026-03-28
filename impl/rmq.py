from collections.abc import Callable

class SparseTable[T]:

    def __init__(self, _a: list[T], _op: Callable[[T, T], T]) -> int:
        a = _a
        op = _op 
        n = len(_a)

        lg = [-1, 0]
        for i in range(2, n + 1):
            lg.append(lg[i // 2] + 1)
        
        table = [[] for i in range(n)] 
        for i in range(n):
            table[i].append(a[i]) 
        for step in range(1, lg[n] + 1):
            for i in range(n - (1 << step) + 1):
                table[i].append(op(table[i][step - 1], table[i + (1 << (step - 1))][step - 1]))

        self.n = n 
        self.op = op 
        self.lg = lg
        self.table = table 



    def query(self, l: int, r: int) -> T:
        assert 0 <= l < r <= self.n 
        z = self.lg[r - l]
        return self.op(self.table[l][z], self.table[r - (1 << z)][z])