class SolutionDetailed:
    def search(self, nums: List[int], target: int) -> int:
        """
        详细版本：包含所有判断逻辑的说明
        """
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # 情况0：直接找到
            if nums[mid] == target:
                return mid
            
            # 情况1：左半部分有序
            # 判断条件：nums[left] <= nums[mid]
            if nums[left] <= nums[mid]:
                # 左半部分：[left, left+1, ..., mid] 是有序的
                # 检查target是否在这个有序范围内
                if nums[left] <= target < nums[mid]:
                    # target在左半有序部分
                    right = mid - 1
                else:
                    # target不在左半部分，去右边找
                    left = mid + 1
            
            # 情况2：右半部分有序
            else:
                # 右半部分：[mid, mid+1, ..., right] 是有序的
                # 检查target是否在这个有序范围内
                if nums[mid] < target <= nums[right]:
                    # target在右半有序部分
                    left = mid + 1
                else:
                    # target不在右半部分，去左边找
                    right = mid - 1
        
        return -1