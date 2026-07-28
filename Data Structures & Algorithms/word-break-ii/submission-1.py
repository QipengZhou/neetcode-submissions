from typing import List
from functools import cache


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        n = len(s)

        @cache
        def dfs(i):
            if i == n:
                return [""]
            res = []
            for word in wordDict:
                if s[i:(i+len(word))] == word:
                    sub_sentences = dfs(i + len(word))
                    for sub in sub_sentences:
                        if sub:
                            res.append(word + " " + sub)
                        else:
                            res.append(word)
            return res
        return dfs(0)
        