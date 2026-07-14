class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        unique_numbers = set()

        for number in nums:
            if number in unique_numbers:
                return number
            unique_numbers.add(number)