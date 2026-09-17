# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prey = None
        curr = head
        while curr: #0
            temp = curr.next #0 -> temp
            curr.next = prey #0->none
            prey = curr #continue
            curr = temp
        return prey






        