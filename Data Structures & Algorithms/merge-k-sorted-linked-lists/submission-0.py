# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeList(self, head1, head2):
        dummy = ListNode()
        prev, cur1, cur2 = dummy, head1, head2
        while cur1 or cur2:
            if cur1 and cur2:
                if cur1.val < cur2.val:
                    cur1.next, prev.next, prev, cur1 = None, cur1, cur1, cur1.next
                else:
                    cur2.next, prev.next, prev, cur2 = None, cur2, cur2, cur2.next
            elif cur1:
                prev.next = cur1
                break
            else:
                prev.next = cur2
                break
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        t = lists[0]
        for v in lists[1:]:
            t = self.mergeList(t, v)
        return t
