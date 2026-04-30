from collections import defaultdict

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        maxIdx = defaultdict(int)
        for i, v in enumerate(s):
            maxIdx[v] = max(i, maxIdx[v])
        sIdx = -1
        eIdx = 0
        for i, v in enumerate(s):
            if maxIdx[v] <= eIdx and i == eIdx:
                res.append(eIdx - sIdx)
                sIdx, eIdx = eIdx, eIdx + 1
            else:
                eIdx = max(eIdx, maxIdx[v])
        return res