class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        x, y = 0, 0
        res = []

        while x < len(word1) and y < len(word2):
            res.append(word1[x])
            x += 1
            res.append(word2[y])
            y += 1

        if x < len(word1):
            res.append(word1[x:])
        else:
            res.append(word2[y:])

        return "".join(res)
