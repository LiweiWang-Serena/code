class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #use union find to check circle
        n = len(edges)
        parent = list(range(n + 1))
        #n = 4. parent = [0,1,2,3, 4]
        #n = 1 parent[1] = 1 parent[1] = 2
        #list = [0, 2, 2, 3, 4]
        #n = 2, parent[1] = 3, parent[1] = 2, parent[2] = 3
        #list = [0, 2, 3, 3, 4]
        #n = 3, parent[3] = 4
        #list = [0, 2, 3, 4, 4]
        #n = 4, parent[2] = 4, parent[2]=3=4
        #list = [0, 2, 3, 4, 4]
        def find(i):
            while parent[i] != i: #find themself without kids
                i = parent[i]
            return i

        #union to find the common parent
        def union(x, y):
            parent[find(x)] = find(y)


        for a, b in edges:
            if find(a) == find(b):
                return[a, b]
            union(a, b)

