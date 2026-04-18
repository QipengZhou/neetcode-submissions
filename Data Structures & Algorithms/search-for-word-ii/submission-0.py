class TreeNode:
    def __init__(self, isEnd=False):
        self.children = {}
        self.isEnd = isEnd


class Trie:
    def __init__(self):
        self.root = TreeNode()
    
    def addWord(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TreeNode()
            node = node.children[c]
        node.isEnd = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.addWord(word)
        rows, cols = len(board), len(board[0])
        visited, res = set(), set()
        def dfs(r, c, node, path):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or board[r][c] not in node.children:
                return
            visited.add((r,c))
            node = node.children[board[r][c]]
            path += board[r][c]
            if node.isEnd:
                res.add(path)
            dfs(r-1, c, node, path)
            dfs(r, c-1, node, path)
            dfs(r+1, c, node, path)
            dfs(r, c+1, node, path)
            visited.remove((r, c))
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, trie.root, "")
        return list(res)
        