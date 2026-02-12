class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        minval = min(nums, key=lambda x: (abs(x), -x))
        return minval