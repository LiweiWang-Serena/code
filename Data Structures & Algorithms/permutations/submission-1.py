class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        used = [None] * n

        def dfs(curr, n):
            if len(curr) == n:
                res.append(curr.copy())
                return
            for i in range(n):
                if not used[i]:
                    used[i] = True
                    curr.append(nums[i])
                    dfs(curr, n)
                    curr.pop()
                    used[i] = None

        dfs([], n)  
        return res

            




        