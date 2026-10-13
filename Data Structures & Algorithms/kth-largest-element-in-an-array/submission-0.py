class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.max_heap = []
        heapq.heapify(self.max_heap)

        for number in nums:
            heapq.heappush(self.max_heap, number)
            if len(self.max_heap) > k:
                heapq.heappop(self.max_heap)
        return heapq.nlargest(k, self.max_heap)[-1]