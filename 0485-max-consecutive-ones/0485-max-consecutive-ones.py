class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = max_rep = 0
        for num in nums:
            if num == 1:
                count += 1
                max_rep = max(max_rep, count)
            else:
                count = 0
        return max_rep