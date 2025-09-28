class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        postfix = [1] * n
        res = [0] * n

        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i]

        postfix[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i]

        for i in range(n):
            left = prefix[i - 1] if i > 0 else 1
            right = postfix[i + 1] if i < n - 1 else 1
            res[i] = left * right

        return res
