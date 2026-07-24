class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        t = []
        n = len(nums)
        visited = [False]*n

        def backtrack():
            if len(t) == n:
                ans.append(t[:])
                return

            for i in range(n):
                if visited[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                    continue
                visited[i] = True
                t.append(nums[i])
                backtrack()
                t.pop()
                visited[i] = False
        backtrack()
        return ans
        