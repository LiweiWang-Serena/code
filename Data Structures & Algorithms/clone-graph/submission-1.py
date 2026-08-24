"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        if not node:
            return None
        def dfs(old_node):
            if old_node in oldToNew:
                return oldToNew[old_node]

            new_node = Node(old_node.val)
            oldToNew[old_node] = new_node
            for old_nei in old_node.neighbors:
                new_node.neighbors.append(dfs(old_nei))
            return new_node

        return dfs(node)
            

        