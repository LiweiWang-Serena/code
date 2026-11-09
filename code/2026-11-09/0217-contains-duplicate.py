# LeetCode 217. Contains Duplicate (Easy)
# Mock OA 2026-11-09: all tests passed
# Time: 3:18

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        return True
