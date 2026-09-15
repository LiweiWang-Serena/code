"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        old_to_newCopy = {}
        curr = head
        while curr:
            old_to_newCopy[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            node = old_to_newCopy[curr]
            node.next = old_to_newCopy[curr.next]
            node.random = old_to_newCopy(curr.random)
            
            curr = curr.next
        return old_to_newCopy [head]





        



