class MyHashMap:
    def __init__(self):
        self.bucket_size = 2069
        self.buckets = [[] for _ in range(self.bucket_size)]

    def _hash(self, key):
        return key % self.bucket_size

    def put(self, key: int, value: int) -> None:
        idx = self._hash(key)
        for k in self.buckets[idx]:
            if k[0] == key:
                k[1] = value
                return
        self.buckets[idx].append([key, value])

    def get(self, key: int) -> int:
        idx = self._hash(key)
        for k in self.buckets[idx]:
            if k[0] == key:
                return k[1]
        return -1

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        for i, k in enumerate(self.buckets[idx]):
            if k[0] == key:
                self.buckets[idx].pop(i)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)