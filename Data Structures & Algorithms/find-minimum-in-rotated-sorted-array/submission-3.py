class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        l = 0
        r = len(nums) - 1
        while r - l != 1:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m
            else:
                r = m
        return min(nums[l], nums[r])