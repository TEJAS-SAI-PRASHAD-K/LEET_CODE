class Solution:
    def helper(self,nums:List[int]) -> int:
        prev2 = 0
        prev1 = 0

        for i in nums:
            cur = max(prev1,prev2+i)
            prev2 = prev1
            prev1 = cur
        return prev1
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[:-1]),self.helper(nums[1:]))