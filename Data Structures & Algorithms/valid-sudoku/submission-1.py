from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_constraints = defaultdict(set)
        col_constraints = defaultdict(set)
        box_constraints = defaultdict(set)
        for i, row in enumerate(board):
            for j, v in enumerate(row):
                if v == '.':
                    continue
                if v in row_constraints[i]:
                    return False
                if v in col_constraints[j]:
                    return False
                box_id = (i//3 * 3) + j // 3
                if v in box_constraints[box_id]:
                    return False
                row_constraints[i].add(v)
                col_constraints[j].add(v)
                box_constraints[box_id].add(v)
        return True