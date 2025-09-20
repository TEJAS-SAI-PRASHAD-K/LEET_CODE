class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp = [0]*n
        pos, neg = 0, 1
        for i in range(n):
            if nums[i] >= 0:
                dp[pos] = nums[i]
                pos += 2
            else:
                dp[neg] = nums[i]
                neg += 2
        return dp