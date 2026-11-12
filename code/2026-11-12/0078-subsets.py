# LeetCode 78. Subsets (Medium)
# Mock OA 2026-11-12: all tests passed
# Time: 5:36

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def dfs(i):
            if i == len(nums):
                res.append(path[:])
                return
            path.append(nums[i])     # 选 nums[i]
            dfs(i+1)
            path.pop()               # 撤销
            dfs(i+1)                   # 不选 nums[i]
        dfs(0)
        return res
