"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])
        s, e = 0, 0
        count, res = 0, 0
        while s < len(intervals):
            if starts[s] < ends[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            if count > res:
                res = count
        return res
        