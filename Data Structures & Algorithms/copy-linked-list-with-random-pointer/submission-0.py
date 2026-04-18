"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        while cur:
            newNode = Node(x=cur.val, next=cur.next)
            cur.next, cur = newNode, cur.next
        cur = head
        while cur:
            t = cur.next
            if cur.random:
                t.random = cur.random.next
            cur = t.next
        dummy = Node(x=0)
        prev, cur = dummy, head
        while cur:
            prev.next, prev, cur.next, cur = cur.next, cur.next, cur.next.next, cur.next.next
        return dummy.next
