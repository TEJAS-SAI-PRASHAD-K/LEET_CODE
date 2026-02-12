class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        minval = nums[0]
        for i in range(1,len(nums)):
            x = abs(nums[i])
            if x < abs(minval):
                minval = nums[i]
            elif x == abs(minval):
                minval = max(minval,nums[i])
            else:
                continue
        return minval