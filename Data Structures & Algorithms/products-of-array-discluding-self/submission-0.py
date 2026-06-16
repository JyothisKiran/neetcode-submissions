class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prdct, zero_cnt = 1, 0
        for num in nums:
                if num:
                    prdct *= num
                else:
                    zero_cnt += 1
        print (zero_cnt, prdct)
        if zero_cnt > 1 : return [0] * len(nums)

        res = [0] * len(nums)

        for i in range(len(nums)):
            if nums[i] :
                res[i] = 0 if zero_cnt else prdct // nums[i]
            else :
                res[i] = prdct

        return res