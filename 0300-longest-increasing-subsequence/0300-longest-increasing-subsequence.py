class Solution:
    def LIS(self,nums: List[int],ind: int,prev: int,dp: List[int][int]) -> int:
        if ind == len(nums):
            return 0
        if dp[ind][prev+1] != -1:
            return dp[ind][prev+1]

        pick = 0
        if prev == -1 or nums[ind] > nums[prev]:
            pick = 1 + self.LIS(nums,ind+1,ind,dp)

        not_picked = self.LIS(nums,ind+1,prev,dp)

        dp[ind][prev+1] = max(pick,not_picked)

        return dp[ind][prev+1]

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = []
        dp = [[-1 for _ in range(n + 1)] for _ in range(n)]
        return self.LIS(nums,0,-1,dp)