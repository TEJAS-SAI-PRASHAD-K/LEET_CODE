class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        summation = (n * (n+1))/2
        res = summation-sum(nums)
        return int(res)