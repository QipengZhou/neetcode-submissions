class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rLow, rHigh = 0, len(matrix)
        while rLow < rHigh:
            rMid = (rLow + rHigh) // 2
            if matrix[rMid][0] == target:
                return True
            elif matrix[rMid][0] < target:
                if (rHigh - rLow) == 1:
                    break
                rLow = rMid
            else:
                rHigh = rMid
        cLow, cHigh = 0, len(matrix[0])
        while cLow < cHigh:
            cMid = (cLow + cHigh) // 2
            if matrix[rLow][cMid] == target:
                return True
            elif matrix[rLow][cMid] < target:
                cLow = cMid + 1
            else:
                cHigh = cMid
        return False