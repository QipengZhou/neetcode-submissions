class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        t = sorted(intervals, key=lambda x: x[0])
        ans = []
        pre = None
        for interval in t:
            if pre is None:
                pre = interval
            elif pre[1] < interval[0]:
                ans.append(pre)
                pre = interval
            else:
                pre[0], pre[1] = min(pre[0], interval[0]), max(pre[1], interval[1])
        ans.append(pre)
        return ans