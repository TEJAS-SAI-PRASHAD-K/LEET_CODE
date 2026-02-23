class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = {}

        for ch in nums:
            freq[ch] = freq.get(ch, 0) + 1

            if freq.get(ch) >= 2:
                return True
        return False