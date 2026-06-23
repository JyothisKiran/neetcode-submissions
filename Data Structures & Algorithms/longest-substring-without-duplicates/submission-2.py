class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 1

        if not s:
            return 0

        seen = {}   
        seen[s[left]] = s[left]
        window_size = len(seen)
        while right< len(s):
            val = s[right]
            if val in seen:
                seen.pop(s[left])
                left += 1
            else:
                seen[val] = val
                right += 1
            
            window_size = max(window_size, len(seen))

        return window_size

