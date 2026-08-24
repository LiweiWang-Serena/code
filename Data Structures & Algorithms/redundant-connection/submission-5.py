class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #union find
        #find the parent of each node
        #union two node in the same group
        #check for cycle, if two node already share the same root, the edge is redundant
        n = len(edges)
        parent = list(range(n + 1)) #list parent to iterate

        def find(i):
            while parent[i] != i:
                parent[i] = parent[parent[i]]
                i = parent[i]
            return i


        def union(a, b):
            parent[find(a)] = find(b)

        #check cycle
        for a, b in edges:
            if find(a) == find(b):
                return [a, b]
            else:
                union(a, b)

       
