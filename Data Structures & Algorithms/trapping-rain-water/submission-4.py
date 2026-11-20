class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        suffix = []
        prefix = []
        prefixMax = height[0]
        suffixMax = height[n-1]

        for i in range(n):
            prefixMax = max(height[i], prefixMax)
            prefix.append(prefixMax)

        for i in range(n, 0, -1):
            suffixMax = max(height[i-1], suffixMax)
            suffix.append(suffixMax)

        trappedWater = 0
        suffix.reverse()
        for i in range(n-1):
            if i == 0 or i == n:
                continue
            trappedWater += min(suffix[i], prefix[i]) - height[i]

        return trappedWater
