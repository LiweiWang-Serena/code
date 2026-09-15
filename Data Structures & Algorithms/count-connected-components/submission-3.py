class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #dfs
        #build graph
        graph = defaultdict(list)
        
        for a,  b in graph[edges]:
            graph[b].append(a)
            graph[a].append(b)

        #dfs nei nodes
        visited = set()
        def dfs(node):
            for nei in graph[node]:
                if node not in visited:
                    visited.add(node)
                    dfs(nei)
        res = ()
        for i in range(n):
            if i not in visited:
                visited.add(node)
                dfs(node)
                res += 1
        return res




        
