class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #find all unique triplets, so we must deduplicated results.
        #ideas, sort the array at first 0(nlog(n)), after sorting, we can skip duplicate 
        #for each fixed i, we use two pointer, move left or rigth base on the sum
        #if sum < 0 move left forward
        #if sum > 0 move right forward
        #if sum == 0, record the triplets, then move both pointer forward to skip duplicated
        result = [] #initialize
        nums.sort()
        n = len(nums) 
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]: #remove duplicate
                continue
            left = i + 1
            right = n - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1 #remove duplicate
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif s > 0:
                    right -= 1
                else:
                    left += 1
        return result
