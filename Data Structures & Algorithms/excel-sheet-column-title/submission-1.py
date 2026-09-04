class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        mapStr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        res = []
        while columnNumber > 0:
            columnNumber -= 1
            remainder = columnNumber % 26
            res.append(mapStr[remainder])
            columnNumber = columnNumber // 26
        return ''.join(reversed(res))