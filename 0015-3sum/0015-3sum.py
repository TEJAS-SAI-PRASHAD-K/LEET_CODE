class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        answer =[]
        for i in range(n):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i] == nums[i-1]:
                continue
            low,hi = i+1,n-1

            while(low < hi):
                total_sum = nums[i] + nums[low] + nums[hi]
                if total_sum == 0:
                    answer.append([nums[i],nums[low],nums[hi]])
                    low,hi = low+1,hi-1
                    while low < hi and nums[low] == nums[low-1]:
                        low += 1
                    while low < hi and nums[hi] == nums[hi+1]:
                        hi -= 1
                elif total_sum < 0:
                    low += 1
                else:
                    hi -= 1
        return answer
            