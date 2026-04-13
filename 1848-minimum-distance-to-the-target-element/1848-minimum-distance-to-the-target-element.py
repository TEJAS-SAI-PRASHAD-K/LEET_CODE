class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        min_val = float('inf')
        for i in range(len(nums)):
            if nums[i] == target:
                min_val = min(min_val,abs(i-start))
            i += 1
        return min_val