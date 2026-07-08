class Solution:
    def search(self, nums: List[int], target: int) -> int:
        while len(nums) > 1:
            mid = int(len(nums)/2)
            if nums[mid] > target:
                nums = nums[:mid]
            elif nums[mid] < target:
                nums = nums[mid:]
            else:
                return mid
            index = mid

        return -1