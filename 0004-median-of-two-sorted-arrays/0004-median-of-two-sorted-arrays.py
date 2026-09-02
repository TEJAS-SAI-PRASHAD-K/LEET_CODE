class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2

        if len(a) > len(b):
            a, b = b, a

        total = len(a) + len(b)
        half = total // 2

        l, r = 0, len(a)

        while l <= r:
            mid_a = (l + r) // 2
            mid_b = half - mid_a

            a_left = a[mid_a - 1] if mid_a > 0 else float("-inf")
            a_right = a[mid_a] if mid_a < len(a) else float("inf")

            b_left = b[mid_b - 1] if mid_b > 0 else float("-inf")
            b_right = b[mid_b] if mid_b < len(b) else float("inf")

            if a_left <= b_right and b_left <= a_right:

                if total % 2:
                    return min(a_right, b_right)

                return (max(a_left, b_left) + min(a_right, b_right)) / 2

            elif a_left > b_right:
                r = mid_a - 1
            else:
                l = mid_a + 1