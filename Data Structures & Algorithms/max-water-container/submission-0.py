class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most_water = 0

        if not heights or len(heights) < 3:
            return 0 if not heights else (min(heights) * 1)

        left_pointer = 0
        right_pointer = len(heights) - 1
        while left_pointer < right_pointer:
            current_water = min(heights[left_pointer], heights[right_pointer]) * (right_pointer - left_pointer)
            if current_water > most_water:
                most_water = current_water
            if heights[left_pointer + 1] > heights[left_pointer]:
                left_pointer += 1
            elif heights[right_pointer - 1] > heights[right_pointer]:
                right_pointer -= 1
            else:
                left_pointer += 1
        return most_water