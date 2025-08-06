class Solution:
    def isPalindrome(self, s: str) -> bool:
        def convert(char: str) -> str:
            if char.isalnum():
                return char.lower()
            return ""
        
        start = 0
        end = len(s) - 1

        while start < end:
            c1 = convert(s[start])
            c2 = convert(s[end])

            if c1 == "":
                start += 1
                continue
            if c2 == "":
                end -= 1
                continue

            if c1 != c2:
                return False

            start += 1
            end -= 1

        return True
