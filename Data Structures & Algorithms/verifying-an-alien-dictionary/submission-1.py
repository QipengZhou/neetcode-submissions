class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderDict = {}
        for i, v in enumerate(order):
            orderDict[v] = i
        def isLess(word1: str, word2: str) -> bool:
            i, j = 0, 0
            while i < len(word1) and j < len(word2) and orderDict[word1[i]] == orderDict[word2[j]]:
                i, j = i+1, j+1
            if i < len(word1) and j < len(word2):
                return orderDict[word1[i]] < orderDict[word2[j]]
            elif i < len(word1):
                return False
            else:
                return True
        for j in range(1, len(words)):
            if not isLess(words[j-1], words[j]):
                return False
        return True