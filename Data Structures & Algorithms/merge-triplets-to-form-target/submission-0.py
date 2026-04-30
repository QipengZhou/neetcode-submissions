class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [0, 0, 0]
        for tri in triplets:
            if tri[0] > target[0] or tri[1] > target[1] or tri[2] > target[2]:
                continue
            res = [max(res[0], tri[0]), max(res[1], tri[1]), max(res[2], tri[2])]
            if res[0] == target[0] and res[1] == target[1] and res[2] == target[2]:
                return True
        return res[0] == target[0] and res[1] == target[1] and res[2] == target[2]