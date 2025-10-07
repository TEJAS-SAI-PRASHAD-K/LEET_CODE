class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n  = len(needle)
        i = 0
        j = i + n - 1
        while i + n <= len(haystack):
            if haystack[i:i+n] == needle:
                return i
            i += 1
        return -1