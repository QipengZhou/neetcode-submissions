from collections import defaultdict

class ListNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        self.freq = 1


class DoublyLinkedList:
    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self._size = 0

    def __len__(self):
        return self._size

    def push_front(self, node: ListNode):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        self._size += 1

    def remove(self, node: ListNode):
        self._size -= 1
        node.prev.next = node.next
        node.next.prev = node.prev

    def pop_tail(self) -> ListNode:
        if self._size == 0:
            return None
        last_node = self.tail.prev
        self.remove(last_node)
        return last_node


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.freq_map = defaultdict(DoublyLinkedList)
        self.min_freq = 0

    def _update_freq(self, node: ListNode):
        old_freq = node.freq
        self.freq_map[old_freq].remove(node)
        if old_freq == self.min_freq and len(self.freq_map[old_freq]) == 0:
            self.min_freq += 1
        node.freq += 1
        self.freq_map[node.freq].push_front(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._update_freq(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._update_freq(node)
            return

        if len(self.cache) >= self.capacity:
            oldest_node = self.freq_map[self.min_freq].pop_tail()
            if oldest_node:
                del self.cache[oldest_node.key]

        new_node = ListNode(key, value)
        self.cache[key] = new_node
        self.freq_map[1].push_front(new_node)
        self.min_freq = 1