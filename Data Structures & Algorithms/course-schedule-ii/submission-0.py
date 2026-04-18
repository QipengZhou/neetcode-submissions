from collections import deque, defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        finishedCourses = 0
        in_degree = [0] * numCourses
        adj = defaultdict(list)
        for course, pre in prerequisites:
            in_degree[course] += 1
            adj[pre].append(course)
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        ans = []
        while queue:
            t = queue.popleft()
            finishedCourses += 1
            ans.append(t)
            for i in adj[t]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    queue.append(i)
        if finishedCourses == numCourses:
            return ans
        return []