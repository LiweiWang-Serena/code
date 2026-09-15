class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
       #the array is sorted in non-dereasing order, so the two pointer scan run in O(N) time.
       #hashmap also gives O(N) time, but need O(N) extra space, since the array is sorted, two pointer are prefered
       left = 0
       rignt = len(numbers) - 1
       while left < right:
        currentSum = numbers[left] + numbers[right]
        if currentSum < target:
            left += 1
        elif currentSum > target:
            right -= 1
        else:
            return[left + 1, right + 1]