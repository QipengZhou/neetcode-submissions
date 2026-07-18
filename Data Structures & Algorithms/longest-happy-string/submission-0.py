import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = []
        if a > 0:
            pq.append((-a, 'a'))
        if b > 0:
            pq.append((-b, 'b'))
        if c > 0:
            pq.append((-c, 'c'))
        heapq.heapify(pq)
        ans = []
        while pq:
            c1, char1 = heapq.heappop(pq)
            if len(ans) >= 2 and ans[-1] == char1 and ans[-2] == char1:
                if not pq:
                    break
                c2, char2 = heapq.heappop(pq)
                ans.append(char2)
                if c2 + 1 < 0:
                    heapq.heappush(pq, (c2+1, char2))
                heapq.heappush(pq, (c1, char1))
            else:
                ans.append(char1)
                if c1 + 1 < 0:
                    heapq.heappush(pq, (c1+1, char1))
        return "".join(ans)
        