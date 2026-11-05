from collections import deque

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = deque(maxlen = capacity)
        self.dict = {}
    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        self.queue.remove(key)
        self.queue.append(key)
        return self.dict[key]
    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict[key] = value
        elif len(self.dict) == self.capacity:
            self.dict.pop(self.queue.popleft())
        self.dict[key] = value
        self.queue.append(key)