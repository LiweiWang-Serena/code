class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        duplicate = set()
        for i in nums:
            if i in duplicate:
                return i
            duplicate.add(i)
        return -1
            


        