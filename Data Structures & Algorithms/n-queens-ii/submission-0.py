class Solution:
    def totalNQueens(self, n: int) -> int:
        total = 0
        cols = set()
        diag1 = set()
        diag2 = set()
        def backtrack(i):
            nonlocal total
            if i == n:
                total += 1
                return
            for c in range(n):
                if c in cols or (i - c) in diag1 or (i + c) in diag2:
                    continue
                cols.add(c)
                diag1.add(i-c)
                diag2.add(i+c)
                backtrack(i+1)
                cols.remove(c)
                diag1.remove(i-c)
                diag2.remove(i+c)
        backtrack(0)
        return total
        