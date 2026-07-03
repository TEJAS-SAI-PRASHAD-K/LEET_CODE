class Solution:
    def longestPrefix(self, s: str) -> str:
        if len(s) == 0:
            return ""
        n = len(s)
        res = ""
        for i in range(1,n+1):
            if s[:i] == s[-i:] and len(s[:i]) != n:
                res = s[:i]
        return res