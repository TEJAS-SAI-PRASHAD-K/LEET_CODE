class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        ind = -1
        n = len(nums)
        for i in range(n-2,-1,-1):
            if(nums[i] < nums[i+1]):
                ind = i
                break
        if ind == -1:
            nums.reverse()
            return
        else:
            for i in range(n-1,ind,-1):
                if(nums[i] > nums[ind]):
                    nums[i], nums[ind] = nums[ind], nums[i]
                    break
        
            nums[ind+1:] = list(reversed(nums[ind+1:]))