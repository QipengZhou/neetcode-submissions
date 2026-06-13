class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)
        for i1 in range(n-3):
            if i1 > 0 and nums[i1] == nums[i1-1]:
                continue
            for i2 in range(i1+1, n-2):
                if i2 > (i1+1) and nums[i2] == nums[i2-1]:
                    continue
                for i3 in range(i2+1, n-1):
                    if i3 > (i2+1) and nums[i3] == nums[i3-1]:
                        continue
                    l, h = i3+1, n
                    t = target - (nums[i1] + nums[i2] + nums[i3])
                    while l < h:
                        mid = (l + h) // 2
                        if nums[mid] == t:
                            ans.append([nums[i1], nums[i2], nums[i3], nums[mid]])
                            break
                        elif nums[mid] < t:
                            l = mid+1
                        else:
                            h = mid
        return ans