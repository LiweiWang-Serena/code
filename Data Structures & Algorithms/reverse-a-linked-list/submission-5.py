# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr: #0
            temp = curr.next #0 -> temp
            curr.next = prev #0->none
            prev = curr #continue
            curr = temp
        return prev






        