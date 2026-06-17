class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = []
        suffix = []
        
        n = len(height)

        prefixMax = height[0]
        suffixMax = height[n-1]

        for i in range(n):
            prefixMax = max(prefixMax, height[i])
            prefix.append(prefixMax)

        for i in range(n, 0 ,-1):
            suffixMax = max(suffixMax, height[i-1])
            suffix.append(suffixMax)

        trappedWater = 0
        suffix.reverse()
        for i in range(n -1):
            if i ==n or i==0:
                continue
            trappedWater += min(prefix[i], suffix[i]) - height[i]

        return trappedWater


