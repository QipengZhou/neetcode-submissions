from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        finishedCourses = 0
        in_degree = [0] * numCourses
        adj = defaultdict(list)
        for course, pre in prerequisites:
            in_degree[course] += 1
            adj[pre].append(course)
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        while queue:
            t = queue.popleft()
            finishedCourses += 1
            for i in adj[t]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    queue.append(i)
        return finishedCourses == numCourses
