class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        n = len(s)
        dp = [1, 1]
        for i in range(1, n):
            t = 0
            if s[i] != '0':
                t += dp[(i-1)%2]
            two_digits = int(s[(i-1):(i+1)])
            if 10 <= two_digits <= 26:
                t += dp[i%2]
            if t == 0:
                return 0
            dp[i%2] = t
        return dp[(n-1)%2]