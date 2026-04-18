class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(i, v, arr):
            if v == target:
                res.append(arr[:])
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                new_v = v + candidates[j]
                if new_v > target:
                    break
                arr.append(candidates[j])
                dfs(j+1, new_v, arr)
                arr.pop()
        dfs(0, 0, [])
        return res