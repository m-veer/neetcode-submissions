from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.output = []
        heapq.heapify(self.output)
        for point in points:
            x1 = point[0]
            y1 = point[1]
            x2 = 0
            y2 = 0
            difference = (x1 - x2)**2 + (y1 - y2)**2
            distance = round(sqrt(abs(difference)),4)
            heapq.heappush(self.output, [-distance, point])
            if len(self.output) > k:
                # Remove smallest from heap
                heapq.heappop(self.output)
        return [self.output[index][1] for index in range(len(self.output))]