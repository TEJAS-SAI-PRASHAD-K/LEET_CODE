class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        res = []
        start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                end = nums[i-1]
                res.append(str(start) if start == end else f"{start}->{end}")
                start = nums[i]

        res.append(str(start) if start == nums[-1] else f"{start}->{nums[-1]}")
        return res
