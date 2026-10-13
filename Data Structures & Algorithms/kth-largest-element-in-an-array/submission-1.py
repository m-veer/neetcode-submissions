class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.max_heap = nums
        heapq.heapify(self.max_heap)
        return heapq.nlargest(k, self.max_heap)[-1]