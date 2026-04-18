from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.mp = defaultdict(list)

    def _getPos(self, key: str, timestamp: int) -> int:
        t = self.mp[key]
        low, high = 0, len(t)
        while low < high:
            mid = (low + high) // 2
            if t[mid][0] == timestamp:
                low = mid
                break
            elif t[mid][0] < timestamp:
                low = mid + 1
            else:
                high = mid
        return low

    def set(self, key: str, value: str, timestamp: int) -> None:
        t = self.mp[key]
        pos = self._getPos(key, timestamp)
        self.mp[key] = t[:pos] + [(timestamp, value)] + t[pos:]

    def get(self, key: str, timestamp: int) -> str:
        pos = self._getPos(key, timestamp)
        if pos < len(self.mp[key]) and self.mp[key][pos][0] <= timestamp:
            return self.mp[key][pos][1]
        elif pos > 0:
            return self.mp[key][pos-1][1]
        return ""
