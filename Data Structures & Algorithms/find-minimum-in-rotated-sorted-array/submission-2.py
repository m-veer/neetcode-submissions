class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        l = 0
        r = len(nums) - 1
        while r - l != 1:
            m = int((l+r)/2)

            mid = nums[m]
            left = nums[l]
            right = nums[r]

            if mid > left and mid < right:
                r = m
            elif mid < left and mid > right:
                l = m
            elif mid >left or mid > right:
                l = m
            elif mid < left or mid < right:
                r = m
        return min(nums[l], nums[r])