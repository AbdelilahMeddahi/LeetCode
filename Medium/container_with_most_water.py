test_case = [4,2,0,3,2,5,2,5]
class Solution:
    def trap(self, height) -> int:
        if not height:
            return 0
        trapped_water=0
        left = 0
        right = len(height)-1
        left_max = height[left]
        right_max = height[right] 
        while left < right:
            if height[left]<height[right]:
                left+=1
                left_max = max(height[left],left_max)
                trapped_water = left_max - height[left]
            else:
                right -= 1
                right_max = max( height[right],right_max)
                trapped_water += right_max - height[right]
        return trapped_water
s = Solution() 
print(s.trap(height = test_case))