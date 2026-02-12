class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        minval = nums[0]
        for i in range(1,len(nums)):
            x = nums[i]
            if abs(x) < abs(minval):
                minval = nums[i]
            elif abs(x) == abs(minval):
                minval = max(minval,x)

        return minval