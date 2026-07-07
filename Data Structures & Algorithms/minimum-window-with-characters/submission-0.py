class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        t_count = {}
        window = {}
        for i in t:
            t_count[i] = t_count.get(i, 0) + 1

        have, need = 0, len(t_count)
        pointers = [-1, -1]
        substr_length = float("infinity")
        left = 0
        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in t_count and window[c] == t_count[c]:
                have+= 1

            while have == need:
                if right - left + 1 < substr_length:
                    pointers = [left, right]
                    substr_length = right - left + 1

                window[s[left]] -= 1

                if s[left] in t_count and window[s[left]] < t_count[s[left]]:
                    have -= 1
                left += 1

        left, right = pointers
        return s[left: right + 1] if substr_length != float("infinity") else ""
                
