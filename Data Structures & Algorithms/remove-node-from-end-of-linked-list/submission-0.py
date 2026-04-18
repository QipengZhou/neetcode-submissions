# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        cur = head
        for _ in range(n):
            cur = cur.next
        prev = dummy
        while cur:
            prev = prev.next
            cur = cur.next
        t = prev.next
        prev.next = t.next
        t.next = None
        return dummy.next