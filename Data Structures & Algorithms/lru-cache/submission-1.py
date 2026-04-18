class ListNode:
    def __init__(self, key: int = 0, val: int = 0, prev: Optional[ListNode] = None, next: Optional[ListNode] = None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next


def deleteNode(v: ListNode) -> None:
    prevNode, nextNode = v.prev, v.next
    prevNode.next = nextNode
    nextNode.prev = prevNode
    v.prev, v.next = None, None


def printLinkedList(head: List[ListNode]):
    cur = head
    while cur:
        print(f"-> ({cur.key}, {cur.val})")
        cur = cur.next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = ListNode(key=-1)
        self.tail = ListNode(key=-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.mp = {}

    def get(self, key: int) -> int:
        if key not in self.mp:
            return -1
        v = self.mp[key]
        # delete node
        deleteNode(v)
        # add to prev tail
        preNode = self.tail.prev
        preNode.next = v
        v.prev = preNode
        v.next = self.tail
        self.tail.prev = v
        return v.val
    
    def addNodeToTail(self, newNode) -> None:
        prevNode = self.tail.prev
        prevNode.next = newNode
        newNode.prev = prevNode
        newNode.next = self.tail
        self.tail.prev = newNode

    def put(self, key: int, value: int) -> None:
        if key not in self.mp:
            if len(self.mp) == self.capacity:
                # delete head next
                v = self.head.next
                deleteNode(v)
                del self.mp[v.key]
            newNode = ListNode(key=key, val=value)
            self.addNodeToTail(newNode)
            self.mp[key] = newNode
        else:
            v = self.mp[key]
            v.val = value
            # delete node
            deleteNode(v)
            # add to tail
            self.addNodeToTail(v)    
