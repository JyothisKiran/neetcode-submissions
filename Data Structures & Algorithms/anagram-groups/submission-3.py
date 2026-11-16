class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            chars = [0] * 26
            for i in s:
                chars[ord(i) - ord('a')] += 1
            res[tuple(chars)].append(s)
        return list(res.values())