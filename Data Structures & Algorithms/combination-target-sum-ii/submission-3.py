class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        nums = candidates
        nums.sort()
        path = []
        total = 0
        def dfs(i, total):
            if total == target:
                res.append(path.copy())
                return
            if total > target or i >= len(nums):
                return
            path.append(nums[i])
            dfs(i + 1, total + nums[i])
            path.pop()
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, total)
        dfs(0, 0)
        return res
            


        