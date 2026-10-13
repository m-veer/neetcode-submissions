class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [-count for count in Counter(tasks).values()]
        heapq.heapify(heap)
        queue = deque()

        cycles = 0

        while heap or queue:
            cycles += 1
            
            if heap:
                count = heapq.heappop(heap) + 1
                if count:
                    queue.append([count, cycles + n])
            if queue and queue[0][1] == cycles:
                heapq.heappush(heap, queue.popleft()[0])
        return cycles