class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start = 0
        nxt = start + 1
        while(start < len(nums)-1):
            if nxt == len(nums):
                start += 1
                nxt = start + 1
                continue
            if nums[start]+nums[nxt] == target:
                return [start,nxt]
            else:
                nxt += 1
        