class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.max_heap = [-stone for stone in stones]
        heapq.heapify(self.max_heap)
        length = len(self.max_heap)
        while length > 1:
            x = heapq.heappop(self.max_heap)
            y = heapq.heappop(self.max_heap)
            length -= 2
            z = y - x
            if z > 0:
                heapq.heappush(self.max_heap, -z)
                length += 1
        return -self.max_heap[0] if length != 0 else 0