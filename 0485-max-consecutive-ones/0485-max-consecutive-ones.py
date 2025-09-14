class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        pt = 0
        count = 0
        max_rep = 0
        while(pt<len(nums)):
            if(nums[pt] == 1):
                count += 1
                pt += 1
                if(max_rep <= count):
                    max_rep = count
            else:
                count = 0
                pt += 1
        
        return max_rep