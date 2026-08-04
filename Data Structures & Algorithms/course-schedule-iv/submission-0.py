from functools import cache
from collections import defaultdict
from typing import List


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(dict)
        for prerequest in prerequisites:
            graph[prerequest[1]][prerequest[0]] = True
        ans = [False] * len(queries)
        @cache
        def isPrerequest(i: int, j: int) -> bool:
            if i in graph[j]:
                return True
            for k in graph[j]:
                if isPrerequest(i, k):
                    return True
            return False
        for i, query in enumerate(queries):
            if isPrerequest(query[0], query[1]):
                ans[i] = True

        return ans
        