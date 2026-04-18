class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        n = nums[-1]
        t = nums[:-1]
        res = self.subsets(t)
        l = len(res)
        for i in range(l):
            v = res[i][:]
            v.append(n)
            res.append(v)
        return res