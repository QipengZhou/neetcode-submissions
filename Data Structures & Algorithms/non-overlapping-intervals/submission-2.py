class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        pre = 0
        ans = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[pre][1]:
                ans += 1
            else:
                pre = i
        return ans