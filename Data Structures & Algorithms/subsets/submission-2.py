class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset_path = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset_path.copy())
                return
            subset_path.append(nums[i])
            dfs(i + 1)
            subset_path.pop()
            dfs(i + 1)
        dfs(0)
        return res








        