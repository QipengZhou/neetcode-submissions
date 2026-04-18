# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cap = 0
        prev, cur1, cur2 = dummy, l1, l2
        while cur1 or cur2:
            if cur1 and cur2:
                t = cur1.val + cur2.val + cap
                cap = t // 10
                newNode = ListNode(val=t % 10)
                prev.next, prev = newNode, newNode
                cur1, cur2 = cur1.next, cur2.next
            else:
                if cur2:
                    cur1 = cur2
                    cur2 = None
                if cap == 0:
                    prev.next = cur1
                    break
                else:
                    t = cur1.val + cap
                    cap = t // 10
                    newNode = ListNode(val=t % 10)
                    prev.next, prev = newNode, newNode
                    cur1 = cur1.next
        if cap > 0:
            newNode = ListNode(val=cap)
            prev.next, prev = newNode, newNode
        return dummy.next
