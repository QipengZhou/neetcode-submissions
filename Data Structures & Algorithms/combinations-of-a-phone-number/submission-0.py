class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mp = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno",
            "7": "pqrs", "8": "tuv", "9": "wxyz",
        }
        res = []
        def backtrack(i, path):
            if i == len(digits):
                if len(path) > 0:
                    res.append(path)
                return
            for j in mp[digits[i]]:
                backtrack(i+1, path+j)
        backtrack(0, "")
        return res