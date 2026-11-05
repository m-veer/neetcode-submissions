from collections import deque

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = deque(maxlen = capacity)
        self.dict = {}
    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        return self.dict[key]
    def put(self, key: int, value: int) -> None:
        if len(self.dict) == self.capacity:
            self.dict.pop(self.queue.popleft())
        self.dict[key] = value
        self.queue.append(key)