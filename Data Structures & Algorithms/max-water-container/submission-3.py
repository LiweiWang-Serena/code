class Solution:
    def maxArea(self, heights: List[int]) -> int:
        reslult = ()
        left = 0
        right = len(heights) - 1
        while left < right:
            h = min(heights[left], height[right])
            area = max(area, h * (r - l))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return result

        
        