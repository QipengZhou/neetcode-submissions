from collections import deque

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[n-1] == '1':
            return False

        queue = deque([0])
        far = 0
        while queue:
            curr = queue.popleft()
            if curr + minJump <= n - 1 <= curr + maxJump:
                return True
            for j in range(max(far+1, curr+minJump), min(n-1, curr+maxJump)+1):
                if s[j] == '0':
                    queue.append(j)
            far = max(far, curr+maxJump)

        return False