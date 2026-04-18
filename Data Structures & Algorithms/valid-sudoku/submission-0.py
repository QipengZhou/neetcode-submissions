from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            rm = defaultdict(bool)
            for v in row:
                if v == '.':
                    continue
                elif rm[v]:
                    return False
                rm[v] = True
        for j in range(9):
            cm = defaultdict(bool)
            for row in board:
                if row[j] == '.':
                    continue
                elif cm[row[j]]:
                    return False
                cm[row[j]] = True
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sm = defaultdict(bool)
                sr, sc = i, j
                for k in range(3):
                    for w in range(3):
                        r, c = sr+k, sc+w
                        if board[r][c] == '.':
                            continue
                        elif sm[board[r][c]]:
                            return False
                        sm[board[r][c]] = True
        return True

