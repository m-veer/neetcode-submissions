class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        output = [0] * len(temperatures)

        for index, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                stack_temperature, stack_index = stack.pop()
                output[stack_index] = index - stack_index
            stack.append([temperature, index])
        return output