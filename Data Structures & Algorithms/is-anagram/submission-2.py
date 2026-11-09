class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False

        count_s , count_t = {}, {}
        
        for i in s:
            if i in count_s:
                count_s[i] = count_s.get(i, 0) + 1
            count_s.setdefault(i,0)

        for i in t:
            if i in count_t:
                count_t[i] = count_t.get(i, 0) + 1
            count_t.setdefault(i,0)
        
        return count_s == count_t
        