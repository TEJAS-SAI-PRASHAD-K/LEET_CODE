from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        sorted_elements = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)
        return sorted_elements[:k]