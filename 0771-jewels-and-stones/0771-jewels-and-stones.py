class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        count = 0

        for ch in stones:
            if ch in jewel_set:
                count += 1

        return count