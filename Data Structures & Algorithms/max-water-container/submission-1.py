class Solution:
    def maxArea(self, heights: List[int]) -> int:
        reslult = ()
        n = len(heights)
        left = 0
        right = n - 1
        while left < right:
            h = min(heights[left], height[right])
            area = max(area, h * (r - l))
            if heights[left] < heght[right]:
                left += 1
            else:
                right -= 1
        return result

        
        