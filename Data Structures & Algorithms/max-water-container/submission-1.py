class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        n =len(heights)
        i = 0
        j = n - 1
        while(i < j):
            distance = j - i
            curr_vol = distance  * min(heights[i],heights[j])
            max = curr_vol if max < curr_vol else max
            if heights[i] < heights[j]:
                i += 1
            else:
                j-= 1
        return max