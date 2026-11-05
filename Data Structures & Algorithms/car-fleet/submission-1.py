from typing import List
from collections import deque

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        d = {}
        for index in range(len(position)):
            d[position[index]] = speed[index]
        d = dict(sorted(d.items(), reverse = True))

        stack = deque()
        fleets = 0

        for key, value in d.items():
            time = (target - key) / value
            if not stack:
                stack.append(time)
                fleets += 1
            if time <= stack[-1]:
                pass
            else:
                stack.append(time)
                fleets += 1
        return fleets