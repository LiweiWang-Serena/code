class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        visited = set()
        for a, b in edges:
            graph[b].append(a)
            graph[a].append(b)

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


        