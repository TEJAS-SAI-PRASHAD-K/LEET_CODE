import math
class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares(x):
            total = 0
            while x > 0:
                total += (x % 10) ** 2
                x //= 10
            return total

        slow = n
        fast = n

        while True:
            slow = sum_of_squares(slow)
            fast = sum_of_squares(sum_of_squares(fast))

            if fast == 1:
                return True
            if slow == fast:
                return False