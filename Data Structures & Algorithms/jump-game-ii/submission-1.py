class Solution:
    def jump(self, nums: List[int]) -> int:
        min_jumps = 0
        max_jumps = 0
        max_jumps_end = 0
        for i in range(len(nums) - 1):
            max_jumps = max(max_jumps, i + nums[i])
            if i == max_jumps_end:
                max_jumps_end = max_jumps
                min_jumps += 1
        return min_jumps

        

        