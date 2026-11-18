class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = "".join(char for char in s if char.isalnum()).lower()
        left = 0
        right = len(s1) - 1
        while (left<right):
            letter = s1[left]
            if s1[right] == letter:
                right-=1
                left+=1
                continue
            else:
                return False

        return True