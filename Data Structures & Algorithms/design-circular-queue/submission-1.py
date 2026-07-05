class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class MyCircularQueue:
    def __init__(self, k: int):
        self.head = ListNode()
        self.capacity = k
        self.num = 0
        self.tail = self.head

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        newNode = ListNode(val=value)
        newNode.prev = self.tail
        self.tail.next = newNode
        self.tail = newNode
        self.num += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        toBeDeleted = self.head.next
        self.head.next = toBeDeleted.next
        if toBeDeleted.next is not None:
            toBeDeleted.next.prev = self.head
        else:
            self.tail = self.head
        self.num -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.next.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.num == 0

    def isFull(self) -> bool:
        return self.num == self.capacity