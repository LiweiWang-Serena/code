class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #union find 
        #first find parent, then union then find def parent
        n = len(edges)
        parent = list(range(n + 1))

        def find(i):
            while parent[i] != i:
                i = parent[i]
            return i

        def union(a, b):
            parent[find(a)] = find(b)


        for a, b in edges:
            if find(a) == find(b):
                return[a, b]
            else:
                union(a, b)

        




