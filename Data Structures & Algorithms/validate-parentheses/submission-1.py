class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        braces = {')': '(', ']': '[', '}': '{'}

        for i in range(len(s)):
            if s[i] in braces and braces[s[i]] not in stk:
                return False
            if s[i] in braces and stk[-1] == braces[s[i]]:
                stk.pop()
                continue
            stk.append(s[i])

        return len(stk) == 0