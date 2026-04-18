# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head):
        prev, cur = None, head
        while cur:
            prev, cur.next, cur = cur, prev, cur.next
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        dummy = ListNode()
        preEnd = dummy
        prev, cur, t = head, head, 1
        while cur:
            if t == k:
                aa = cur.next
                cur.next = None
                th = self.reverse(prev)
                prev.next = aa
                preEnd.next, preEnd = th, prev
                prev, cur, t = aa, aa, 1
            else:
                cur = cur.next
                t += 1
        return dummy.next
        