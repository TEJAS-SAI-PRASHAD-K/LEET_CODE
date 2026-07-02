class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        # for i in range(len(s)):
        #     if s[i] == '(':
        #         stack.append('(')
        #     elif s[i] == ')':
        #         if len(stack) == 0:
        #             stack.append(')')
        #         else:
        #             stack.pop()
        
        # return len(stack)
        openp = 0
        closedp = 0

        for i in range(len(s)):
            if s[i] == '(':
                openp += 1
            elif s[i] == ')':
                if openp == 0:
                    closedp += 1
                else:
                    openp -= 1
        
        return abs(closedp+openp)