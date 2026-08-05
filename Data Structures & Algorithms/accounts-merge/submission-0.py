from collections import defaultdict
from typing import List


class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x: str) -> str:
        if self.parent.setdefault(x, x) != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: str, y: str):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        email_to_name = {}
        for acc in accounts:
            name = acc[0]
            first_email = acc[1]
            for email in acc[1:]:
                email_to_name[email] = name
                uf.union(first_email, email)

        components = defaultdict(list)
        for email in email_to_name:
            root = uf.find(email)
            components[root].append(email)
        ans = []
        for root, emails in components.items():
            ans.append([email_to_name[root]] + sorted(emails))
        return ans
        