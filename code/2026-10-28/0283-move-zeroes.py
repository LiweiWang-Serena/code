# LeetCode 283. Move Zeroes (Easy)
# Mock OA 2026-10-28: all tests passed
# Time: 25:17
#
# 2. Data structures: list
# 3. Algorithm: slow fast pointer
# 4. Time and space complexity: time 0(n) space 0(n)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        s = 0
        for f in range(len(nums)):
                if nums[f] != 0:
                    nums[s],nums[f] = nums[f],nums[s]
                    s += 1
