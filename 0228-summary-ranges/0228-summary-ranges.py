class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        num_start = nums[0]
        num_end = num_start
        res = []
        for i in range(1,len(nums)):
            if nums[i] == num_end+1:
                num_end = nums[i]
            else:
                if num_end == num_start:
                    res.append(f"{num_start}")
                else:
                    res.append(f"{num_start}->{num_end}")
                num_start = nums[i]
                num_end = nums[i] 
        if num_end == num_start:
            res.append(f"{num_start}")
        else:
            res.append(f"{num_start}->{num_end}")
        return res
