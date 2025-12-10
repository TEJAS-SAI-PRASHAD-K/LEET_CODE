class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        unique_nums1 = set(nums1)
        unique_nums2 = set(nums2)
        hashset = {}

        for i in unique_nums1:
            hashset[i] = hashset.get(i, 0) + 1

        res = []
        for i in unique_nums2:
            if i in hashset:
                res.append(i)

        return res
