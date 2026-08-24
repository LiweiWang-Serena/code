class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #check edge = n - 1 (no cycle)
        if len(edges) != n - 1:
            return False

        #bulid graph
        graph = defaultdict(list)
        q = deque([0])
        for a, b in edges:
            graph[b].append(a)
            graph[a].append(b)


        #bfs 
        visited = set()
        visited.add(0)
        while q:
            node = q.popleft()
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    q.append(nei)


        if len(visited) == n:
            return True
        else:
            return False

        
        