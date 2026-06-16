class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen ={}
        max=0
        if not len(nums):
            return 0
        for i in sorted(nums):
                if i in seen:
                    continue
                if i-1 in seen:
                    val = seen.pop(i-1)
                    val.append(i)
                    seen.setdefault(i,val) 
                    continue
                seen.setdefault(i,[i])
        for val in seen.values():
            max= max if max > len(val) else len(val)
        return max
        