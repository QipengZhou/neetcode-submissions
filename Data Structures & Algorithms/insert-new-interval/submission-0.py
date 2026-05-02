class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l, r = 0, len(intervals)
        while l < r:
            mid = (l + r) // 2
            if intervals[mid][0] <= newInterval[0]:
                l = mid + 1
            else:
                r = mid
        ans = []
        for i in range(0, l-1):
            ans.append(intervals[i])
        i = max(0, l - 1)
        added = False
        while i < len(intervals):
            if intervals[i][0] > newInterval[1]:
                if not added:
                    ans.append(newInterval)
                    added = True
                ans.append(intervals[i])
            elif intervals[i][1] < newInterval[0]:
                ans.append(intervals[i])
            else:
                newInterval[0] = min(intervals[i][0], newInterval[0])
                newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        if not added:
            ans.append(newInterval)
        return ans