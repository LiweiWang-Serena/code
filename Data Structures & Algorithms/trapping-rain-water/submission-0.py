from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        water = 0
        while l < r:
            if leftMax <= rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                water += max(0, leftMax - height[l])   # == min(leftMax,rightMax)-height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                water += max(0, rightMax - height[r])  # == min(leftMax,rightMax)-height[r]
        return water
