class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_pointer = 0
        right_pointer = left_pointer + 1
        while left_pointer <= len(numbers):
            if numbers[left_pointer] + numbers[right_pointer] == target:
                return [left_pointer + 1, right_pointer + 1]
            right_pointer += 1
            if right_pointer >= len(numbers):
                left_pointer += 1
                right_pointer = left_pointer + 1