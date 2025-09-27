from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        sorted_nums = sorted(nums, key=lambda x: (freq[x], x), reverse=True)

        res = []
        i = 0
        j = 0

        while i < k and j < len(sorted_nums):
            if not res or res[-1] != sorted_nums[j]:
                res.append(sorted_nums[j])
                i += 1
            j += 1

        return res
