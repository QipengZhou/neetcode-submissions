import heapq
from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ans, pq = [], []
        sorted_tasks = []
        for i, task in enumerate(tasks):
            sorted_tasks.append([task[0], task[1], i])
        sorted_tasks.sort(key=lambda x: x[0])
        time = 0
        task_idx = 0
        n = len(tasks)
        while task_idx < n or pq:
            if not pq and time < sorted_tasks[task_idx][0]:
                time = sorted_tasks[task_idx][0]
            while task_idx < n and sorted_tasks[task_idx][0] <= time:
                enqueue_time, proc_time, orig_idx = sorted_tasks[task_idx]
                heapq.heappush(pq, (proc_time, orig_idx))
                task_idx += 1

            proc_time, orig_idx = heapq.heappop(pq)
            ans.append(orig_idx)
            time += proc_time
        return ans