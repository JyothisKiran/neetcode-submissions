class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums) - 1
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                    continue
            first = nums[i]
            left = i+1
            right = n
            while (left< right):

                curr_sum = nums[left] + nums[right]
                if (curr_sum < -first):
                    left+=1
                    continue
                elif (curr_sum > -first):
                    right-=1
                    continue
                else:
                    res.append([first, nums[left], nums[right]])
                    right-=1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return res