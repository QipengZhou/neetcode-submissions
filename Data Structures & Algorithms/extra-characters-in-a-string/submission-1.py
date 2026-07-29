class TreeNode:
    def __init__(self, isEnd=False):
        self.children = {}
        self.isEnd = isEnd


class Trie:
    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TreeNode()
            node = node.children[c]
        node.isEnd = True


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie()
        for word in dictionary:
            trie.addWord(word)
        n = len(s)
        dp = [0]*(n+1)
        for i in range(n-1, -1, -1):
            dp[i] = dp[i+1] + 1
            node = trie.root
            for j in range(i, n):
                char = s[j]
                if char not in node.children:
                    break
                node = node.children[char]
                if node.isEnd:
                    dp[i] = min(dp[i], dp[j+1])
        return dp[0]