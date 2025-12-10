import math
class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(x):
            total = 0
            while x > 0:
                total += (x % 10) ** 2
                x //= 10
            return total

        slow = n
        fast = get_next(n)

        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))

        return fast == 1