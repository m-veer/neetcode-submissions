class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = 0

        while len(nums) > 1:
            mid = int(len(nums)/2)
            if nums[mid] > target:
                nums = nums[:mid]
                index -= mid
            elif nums[mid] < target:
                nums = nums[mid:]
                index += mid
            else:
                return index + mid
            # index += mid

        return -1