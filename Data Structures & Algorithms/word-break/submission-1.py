from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        @lru_cache()
        def canBreak(subStr) -> bool:
            if subStr == "":
                return True
            for word in wordSet:
                if subStr.endswith(word) and canBreak(subStr[:-len(word)]):
                    return True
            return False
        return canBreak(s)