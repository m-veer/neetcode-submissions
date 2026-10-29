class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1 or len(nums) == 1:
            return nums

        heap = []
        output = []

        for index in range(k-1):
            heapq.heappush(heap, (-nums[index], index))

        for index in range(k-1, len(nums)):
            heapq.heappush(heap, (-nums[index], index))
            while True:
                largest = heapq.nsmallest(1, heap)
                if largest[0][1] < index - k + 1:
                    heapq.heappop(heap)
                else:
                    output.append(-largest[0][0])
                    break
        return output