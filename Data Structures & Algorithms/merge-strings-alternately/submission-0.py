class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1, n2 = len(word1), len(word2)
        t = []
        for c1, c2 in zip(word1, word2):
            t.append(c1)
            t.append(c2)
        res = ''.join(t)
        if n1 > n2:
            res += word1[n2:]
        elif n2 > 1:
            res += word2[n1:]
        return res
        