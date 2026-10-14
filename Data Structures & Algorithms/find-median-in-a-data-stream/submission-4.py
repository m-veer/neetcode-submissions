class MedianFinder:
    def __init__(self):
        self.left = [] # max heap (negated), smaller half
        self.right = [] # min heap, larger half
    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)
        # move left's max to right to keep ordering
        heapq.heappush(self.right, -heapq.heappop(self.left))
        # rebalance so left has equal or one more element
        if len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))
    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return float(-self.left[0])
        return (-self.left[0] + self.right[0]) / 2