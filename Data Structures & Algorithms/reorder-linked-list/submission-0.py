# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getLen(self, head: Optional[ListNode]) -> int:
        length, cur = 0, head
        while cur:
            length += 1
            cur = cur.next
        return length
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head
        while cur:
            cur.next, cur, prev = prev, cur.next, cur
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        n = self.getLen(head)
        a = n // 2
        prev = head
        for _ in range(a):
            prev = prev.next
        cur = head
        while prev.next:
            cur = cur.next
            prev = prev.next
        secondList = self.reverseList(cur.next)
        cur.next = None
        cur1, cur2 = head, secondList
        while cur2:
            cur1.next, cur1, cur2.next, cur2 = cur2, cur1.next, cur1.next, cur2.next
        