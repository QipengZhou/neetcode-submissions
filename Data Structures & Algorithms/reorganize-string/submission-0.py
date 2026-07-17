import collections
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = collections.Counter(s)

        maxHeap = [[-count, char] for char, count in counter.items()]
        heapq.heapify(maxHeap)

        ans = []
        prev = None

        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            ans.append(char)
            count += 1

            if prev and -prev[0] > 0:
                heapq.heappush(maxHeap, prev)

            prev = [count, char]
        result = "".join(ans)
        return result if len(result) == len(s) else ""
        