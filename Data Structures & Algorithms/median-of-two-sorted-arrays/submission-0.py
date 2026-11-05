class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A) - 1

        while True:
            A_m = (l + r) // 2
            B_m = half - A_m - 2

            A_left = A[A_m] if A_m >= 0 else float("-infinity")
            A_right = A[A_m + 1] if (A_m + 1) < len(A) else float("infinity")
            B_left = B[B_m] if B_m >= 0 else float("-infinity")
            B_right = B[B_m + 1] if (B_m + 1) < len(B) else float("infinity")

            if A_left <= B_right and B_left <= A_right:
                # Valid partition
                if total % 2:
                    # odd
                    return min(A_right, B_right)
                else:
                    # even
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2
            elif A_left > B_right:
                r = A_m - 1
            else:
                l = A_m + 1