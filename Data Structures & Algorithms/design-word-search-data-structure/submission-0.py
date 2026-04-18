class TreeNode:
    def __init__(self, isEnd=False):
        self.children = {}
        self.isEnd = isEnd


class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TreeNode()
            node = node.children[c]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.root
        def dfs(i, node) -> bool:
            if i == len(word):
                return node.isEnd
            if word[i] == '.':
                for child in node.children:
                    if dfs(i+1, node.children[child]):
                        return True
                return False
            if word[i] not in node.children:
                return False
            return dfs(i+1, node.children[word[i]])
        return dfs(0, node)
        
