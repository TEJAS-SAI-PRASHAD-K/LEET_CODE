class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        ans = 0

        neg = (dividend < 0) ^ (divisor < 0)

        a = abs(dividend)
        b = abs(divisor)

        for i in range(31, -1, -1):

            if b << i <= a:
                a -= b << i
                ans += 1 << i

        if neg:
            ans = -ans

        if ans > 2147483647:
            ans = 2147483647

        return ans