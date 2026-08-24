class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #union find 
        #first def parent arrange and base case
        n = len(edges)
        parent = list(range(n + 1))
        #then def parent
        def find(i):
            while parent[i] != i:
                i = parent[i]
            return i

        #then def union
        def union(a, b):
            parent[find(a)] = find(b)


        #then find circle
        for a, b in edges:
            if find(a) == find(b):
                return [a, b]
            else:
                union(a, b)

        




