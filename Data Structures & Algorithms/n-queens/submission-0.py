class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        def backtrack(i, path, cols, posDiag, negDiag):
            if i == n:
                print(path)
                res.append(list(path))
                return
            t = ["."] * n
            for j in range(n):
                if cols.get(j, False) or posDiag.get(i+j, False) or negDiag.get(i-j, False):
                    continue
                t[j] = "Q"
                cols[j] = True
                posDiag[i+j] = True
                negDiag[i-j] = True
                path.append("".join(t))
                backtrack(i+1, path, cols, posDiag, negDiag)
                t[j] = "."
                cols[j] = False
                posDiag[i+j] = False
                negDiag[i-j] = False
                path.pop()
        backtrack(0, [], {}, {}, {})
        return res