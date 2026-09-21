class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        left_pointer = 0
        right_pointer = left_pointer + 1

        highest = 0
        water = 0
        lower_passed = False

        while right_pointer < len(height):
            if height[right_pointer] >= highest:
                highest = height[right_pointer]

                # Check the length and calculation of the wall
                if lower_passed:
                    temp_sum = sum(height[left_pointer + 1: right_pointer])
                    water += min(height[left_pointer], height[right_pointer]) * (right_pointer - left_pointer - 1) - temp_sum
                    lower_passed = not lower_passed
                
                left_pointer = right_pointer
            elif height[right_pointer] < highest:
                lower_passed = True
                well = height[left_pointer + 1: right_pointer]
                max_height = 0 if not height[right_pointer+1:] else max(height[right_pointer+1:])
                if (height[right_pointer] in well) and not max_height >= height[left_pointer]:
                    left_pointer += well.index(height[right_pointer]) + 1
                    temp_sum = sum(height[left_pointer + 1: right_pointer])
                    water += min(height[left_pointer], height[right_pointer]) * (right_pointer - left_pointer - 1) - temp_sum
                    lower_passed = not lower_passed
                    left_pointer = right_pointer
            right_pointer += 1
        return water