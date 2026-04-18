# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        prev = dummy
        cur1, cur2 = list1, list2
        while cur1 or cur2:
            if cur1 is None:
                prev.next = cur2
                break
            elif cur2 is None:
                prev.next = cur1
                break
            elif cur1.val < cur2.val:
                cur1.next, prev.next, cur1, prev = None, cur1, cur1.next, cur1
            else:
                cur2.next, prev.next, cur2, prev = None, cur2, cur2.next, cur2 
        return dummy.next