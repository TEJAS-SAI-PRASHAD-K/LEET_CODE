class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start = 0
        end = k - 1
        arrsum = sum(nums[start:end+1])
        maxSum = arrsum
        while(end+1 < len(nums)):
            arrsum = arrsum - nums[start]
            start += 1
            end += 1
            arrsum = arrsum + nums[end]
            maxSum = max(maxSum,arrsum)
        return maxSum/k