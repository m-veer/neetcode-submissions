class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) < 2:
            return 0 if nums[0] == target else -1
        # Find pivot index
        def findMin(nums: List[int]) -> int:
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
            return l if nums[l] < nums[r] else r
        pivot = findMin(nums)

        # Since now we have the pivot index, find the target
        if nums[pivot] == target:
            return pivot
        
        l = 0
        r = len(nums) - 1
        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        else:
            r = pivot - 1
        while l <= r:
            m = int((l+r)/2)
            left = nums[l]
            right = nums[r]
            mid = nums[m]

            if mid == target:
                return m
            if mid < target:
                l = m + 1
            else:
                r = m - 1
        return -1