class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        for _ in range(k+1):
            temp_prices = prices[:]
            for u, v, w in flights:
                if prices[u] == float('inf'):
                    continue
                if prices[u] + w < temp_prices[v]:
                    temp_prices[v] = prices[u] + w
            prices = temp_prices

        return -1 if prices[dst] == float('inf') else prices[dst]