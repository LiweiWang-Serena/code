class Solution:
    def maxArea(self, heights: List[int]) -> int:
        reslult = ()
        n = len(height)
        left = 0
        right = n - 1
        while left < right:
            h = min(height[left], height[right])
            area = max(area, h * (r - l))
            if height[left] < heght[right]:
                left += 1
            else:
                right -= 1
        return result

        
        