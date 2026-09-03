import heapq
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        unused_rooms = list(range(n))
        heapq.heapify(unused_rooms)

        used_rooms = []

        count = [0] * n

        for start, end in meetings:
            duration = end - start
            while used_rooms and used_rooms[0][0] <= start:
                _, room = heapq.heappop(used_rooms)
                heapq.heappush(unused_rooms, room)

            if unused_rooms:
                room = heapq.heappop(unused_rooms)
                heapq.heappush(used_rooms, (end, room))
            else:
                earliest_end, room = heapq.heappop(used_rooms)
                heapq.heappush(used_rooms, (earliest_end + duration, room))

            count[room] += 1
        max_meetings = max(count)
        return count.index(max_meetings)