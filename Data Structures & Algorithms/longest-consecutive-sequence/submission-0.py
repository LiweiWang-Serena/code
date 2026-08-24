class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums) #change nums to set
        res = 0 #initialize result 
        for i in nums:
            if i - 1 in nums:
                continue
            else:
                current = i
                count = 0
                while current in nums:
                    current += 1
                    count += 1
            res = max(res, count)
        return res
            
