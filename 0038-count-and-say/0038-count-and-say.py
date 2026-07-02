class Solution:
    def rle(self,s:str) -> str:
        new_str = ""
        temp = s[0]
        count = 0
        for i in range(0,len(s)):
            if temp == s[i]:
                count += 1
            else:
                new_str += (f"{count}{temp}")
                temp = s[i]
                count = 1
        new_str += (f"{count}{temp}")
        
        return new_str

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        prev = self.countAndSay(n - 1)
        return self.rle(prev)