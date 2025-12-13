class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        substring_set = set()
        max_len = 0

        for r in range(len(s)):
            while s[r] in substring_set:
                substring_set.remove(s[l])
                l += 1
            
            substring_set.add(s[r])
            max_len = max(max_len,r-l+1)
        return max_len
        