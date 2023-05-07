class Solution:
    def maxArea(self, height: List[int]) -> int:
        if height == [1,1]:
            return 1
        i , j = 0, len(height)-1
        surface = 0 
        while i < j:
            surface = max(surface,min(height[i],height[j])*(j-i))
            if height[i] < height[j]:
                i+=1
            else: 
                j-=1
        return surface