# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        dummy = ListNode(next=head)
        pre, ln = dummy, head
        for _ in range(left-1):
            pre = pre.next
        ln_pre = pre
        ln = pre.next
        rn = ln
        for _ in range(left, right):
            rn = rn.next
        cur = ln
        print(cur.val, ln.val, rn.val)
        while pre != rn:
            cur.next, cur, pre = pre, cur.next, cur
        ln_pre.next, ln.next = pre, cur
        return dummy.next
        