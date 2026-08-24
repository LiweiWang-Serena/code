class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums) #convet lsit to set to store element because the avrage time complexity is O(1)
        res = 0 #initialize the result to keep track of the longest 
        for i in nums: # now nums is already set, and we iterate i in the set
            if i - 1 in nums: #we iterate i - 1 in nums, why i - 1, because i - 1 in nums means they are not start
                continue #we skip it using continue
            else:
                current = i
                count = 0 #if i - 1 is not in the set, then i is the start of the sequence
                while current in nums: #use while to iterate set nums because we dont know how many iterate are needed
                    current += 1
                    count += 1 #when current is in the set, we increase both current and count by i to go through the entire consecutive sequence
                res = max(res, count) # we update res with the maximum of result and count
        return res 
