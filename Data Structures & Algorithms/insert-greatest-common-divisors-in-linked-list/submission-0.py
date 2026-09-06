# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        pre, cur = head, head.next
        while cur is not None:
            new_node = ListNode(math.gcd(pre.val, cur.val))
            new_node.next = cur
            pre.next = new_node
            pre, cur = cur, cur.next
        return head