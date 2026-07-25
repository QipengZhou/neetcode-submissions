class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        s = 0
        for v in matchsticks:
            s += v
        if s % 4 != 0:
            return False
        edgeLength = s // 4
        matchsticks.sort(reverse=True)
        if matchsticks[0] > edgeLength:
            return False
        sides = [0] * 4
        n = len(matchsticks)
        def backtrack(i):
            if i == n:
                return True
            match = matchsticks[i]
            for j in range(4):
                if sides[j] + match <= edgeLength:
                    sides[j] += match
                    if backtrack(i+1):
                        return True
                    sides[j] -= match
                if sides[j] == 0:
                    break
            return False
        return backtrack(0)
        