class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        x = 0
        y = 0

        res = ""

        while(x != len(word1) and y != len(word2)):
            res = res+word1[x]
            x += 1
            res = res+word2[y]
            y += 1
        if x != len(word1):
            res += word1[x:len(word1)]
        else:
            res += word2[y:len(word2)]

        return res
        
        