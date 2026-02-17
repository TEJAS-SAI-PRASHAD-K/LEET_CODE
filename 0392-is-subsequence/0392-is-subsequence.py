class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        res = True
        i = 0
        j = 0

        while(i<len(s) and j<len(t)):
            if(s[i] == t[j]):
                res = True
                i += 1
            j += 1

        if(i != len(s)):
            res = False
        return res
        

