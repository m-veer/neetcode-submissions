class MedianFinder:
    def __init__(self):
        # Left + Right
        # MaxHeap + MinHeap
        # Right most (Biggest) is important + Left most is important (Smallest)

        self.min_heap = []
        self.max_heap = []
        heapq.heapify(self.min_heap)
        heapq.heapify(self.max_heap)
    def addNum(self, num: int) -> None:
        # If first heap is empty, append to first heap, else if second heap is empty, append to second
        # Later choose heaps the basis number
        # MaxHeap: should be added if number is less than max
        # MinHeap: should be added if number is greater than max
        # Else choose any

        # if not self.max_heap or num > heapq.nlargest(1, self.max_heap)[0]:
        #     heapq.heappush(self.max_heap, num)
        # else:
        #     heapq.heappush(self.min_heap, num)
        
        if not self.max_heap:
            heapq.heappush(self.max_heap, num)
        elif not self.min_heap:
            if num < self.max_heap[0]:
                temp_num = heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, temp_num)
                heapq.heappush(self.max_heap, num)
            else:
                heapq.heappush(self.min_heap, num)
        elif num > heapq.nlargest(1, self.max_heap)[0] and num >= heapq.nlargest(1, self.min_heap)[0]:
            heapq.heappush(self.min_heap, num)
        elif num >= heapq.nlargest(1, self.max_heap)[0] and num < heapq.nlargest(1, self.min_heap)[0]:
            heapq.heappush(self.max_heap, num)
        elif num <= heapq.nlargest(1, self.max_heap)[0] and num < heapq.nlargest(1, self.min_heap)[0]:
            heapq.heappush(self.max_heap, num)
        if abs(len(self.min_heap) - len(self.max_heap)) > 1:
            smaller_heap = self.min_heap if len(self.max_heap) > len(self.min_heap) else self.max_heap
            bigger_heap = self.min_heap if len(self.min_heap) > len(self.max_heap) else self.max_heap
            temp_index = bigger_heap.index(heapq.nlargest(1, bigger_heap)[0]) if bigger_heap == self.max_heap else 0
            temp = bigger_heap[temp_index]
            del bigger_heap[temp_index]
            heapq.heappush(smaller_heap, temp)
        # print()
    def findMedian(self) -> float:
        # If both heaps aren't empty, check the total length and calculate mediam
        total_length = len(self.min_heap) + len(self.max_heap)
        # first_number = heapq.nlargest(1, self.max_heap)[0]
        # second_number = heapq.nlargest(1, self.min_heap)[0]
        if total_length < 2:
            return float(self.min_heap[0] if self.min_heap else self.max_heap[0])
        elif total_length%2 == 0:
            # Even -> find mean
            first_number = heapq.nlargest(1, self.max_heap)[0]
            second_number = heapq.nsmallest(1, self.min_heap)[0]
            return float((first_number + second_number)/2)
        elif total_length%2 != 0:
            # Odd -> return the largest number of whichever list is bigger
            # print()
            return float(heapq.nlargest(1, self.max_heap)[0] if len(self.max_heap) > len(self.min_heap) else heapq.nsmallest(1, self.min_heap)[0])