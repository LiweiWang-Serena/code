class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #firstly ，we consider about to use set,bucause do not alloes to use duplicate
        #if a number is already in set, return true,  otherwise, add to set
        # checking and add elements to hashsethas an average time complexity of O(1)
        #sorting the array could also work, but time complexity at least is O n(logn),due to the sorting step
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False


