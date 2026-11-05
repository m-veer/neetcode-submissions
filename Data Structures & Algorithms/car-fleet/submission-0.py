from typing import List
from collections import deque

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = deque()
        fleets = 0

        for index in range(len(position)):
            time = (target - position[index]) / speed[index]
            if not stack:
                stack.append(time)
                fleets += 1
            if time <= stack[-1]:
                pass
            else:
                stack.append(time)
                fleets += 1
        return fleets