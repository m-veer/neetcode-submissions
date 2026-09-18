class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most_water = 0

        if not heights or len(heights) < 3:
            return 0 if not heights else (min(heights) * 1)

        left_pointer = 0
        right_pointer = len(heights) - 1

        is_left = True
        while left_pointer < right_pointer:
            # print(heights[left_pointer], heights[right_pointer])
            current_water = min(heights[left_pointer], heights[right_pointer]) * (right_pointer - left_pointer)
            if current_water > most_water:
                most_water = current_water

            if heights[left_pointer + 1] > heights[left_pointer]:
                left_pointer += 1
            elif heights[right_pointer - 1] > heights[right_pointer]:
                right_pointer -= 1
            else:
                if is_left and left_pointer + 1 < len(heights)//2:
                    left_pointer += 1
                else:
                    right_pointer -= 1
                is_left = not is_left
        return most_water