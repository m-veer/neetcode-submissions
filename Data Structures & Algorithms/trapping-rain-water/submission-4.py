class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        water = 0
        l, r = 0, len(height) - 1
        l_max, r_max = height[l], height[r]

        while l < r:
            if l_max < r_max:
                l += 1
                l_max = max(l_max, height[l])
                water += l_max - height[l]
            else:
                r -= 1
                r_max = max(r_max, height[r])
                water += r_max - height[r]
        return water