class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        self.heap = tasks
        heapq.heapify(self.heap)

        self.queue = deque()

        self.output = []

        self.cycles = 0

        while self.heap or self.queue:
            if self.heap:
                task = heapq.heappop(self.heap)

                if task not in self.output[-n:]:
                    self.output.append(task)
                    self.cycles += 1
                else:
                    self.queue.append(task)
            else:
                task = self.queue.popleft()
                if task not in self.output[-n:]:
                    self.output.append(task)
                    self.cycles += 1
                else:
                    while task in self.output[-n:]:
                        self.output.append(None)
                        self.cycles += 1
                    self.output.append(task)
                    self.cycles += 1
        return self.cycles