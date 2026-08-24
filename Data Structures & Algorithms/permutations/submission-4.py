class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        used = [False] * n
        def dfs(curr):
            if len(curr) == n:
                res.append(curr.copy())
                return
            for i in range(n):
                if not used[i]:
                    used[i] = True
                    curr.append(nums[i])
                    dfs(curr)
                    curr.pop()
                    used[i] = False
        dfs([])
        return res

            


        


      

            




        