class Solution:
    def romanToInt(self, s: str) -> int:
        rmtoint = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

        total = 0
        for i in range(len(s)-1):
            cur_val = rmtoint[s[i]]
            next_val = rmtoint[s[i+1]]

            if cur_val < next_val:
                total -= cur_val
            else:
                total += cur_val
        total += rmtoint[s[-1]]
        return total