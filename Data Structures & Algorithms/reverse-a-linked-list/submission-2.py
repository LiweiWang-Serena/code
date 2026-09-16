# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        Prev = None #define a dummy node for reserve
        curr = head
        while curr:
            temp = curr.next
             #initial temp
            curr.next = Prev #0-dummy
            Prev = curr #
            curr = temp
        return Prev




        