class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        max_jump = 0
        end = 0
        for i in range(len(nums) - 1):
            

            max_jump = max(max_jump, i + nums[i])
            if i == end:
                count += 1
                end = max_jump
        return count


        