class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #dfs
        #build graph
        graph = defaultdict(list)
        
        for a,  b in edges:
            graph[b].append(a)
            graph[a].append(b)

        #dfs nei nodes
        visited = set()
        def dfs(node):
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
        res = 0
        for node in range(n):
            if node not in visited:
                visited.add(node)
                dfs(node)
                res += 1
        return res




        
