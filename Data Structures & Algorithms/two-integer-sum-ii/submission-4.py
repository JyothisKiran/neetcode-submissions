class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if ( complement in seen ):
                return (sorted([i+1, seen[complement]+1]))
            seen.setdefault(nums[i], i)
        return []