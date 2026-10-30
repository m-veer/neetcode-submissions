class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        m = int((l+r)/2)

        while nums[m] != target:
            left = nums[l]
            right = nums[r]
            
            if r - l == 1:
                if left == target:
                    return l
                elif right == target:
                    return r
                else:
                    return -1

            if target < right:
                l = m
            else:
                r = m
            m = int((l+r)/2)
        return m