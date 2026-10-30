class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)

        while lo < hi:
            mid = (lo + hi) // 2
            hours = sum((p + mid - 1) // mid for p in piles)  # ceil(p / mid)

            if hours <= h:
                hi = mid        # mid works; try slower (but keep mid as a candidate)
            else:
                lo = mid + 1    # mid is too slow; must go faster

        return lo