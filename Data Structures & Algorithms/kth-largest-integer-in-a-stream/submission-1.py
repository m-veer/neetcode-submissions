class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.nums = [-number for number in nums]
        self.k = k
        heapq.heapify(self.nums)
    def add(self, val: int) -> int:
        heapq.heappush(self.nums, -val)
        return -heapq.nsmallest(self.k, self.nums)[self.k - 1]