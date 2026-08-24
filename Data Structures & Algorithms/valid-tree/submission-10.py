class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #check cycle
        #check connect
        if len(edges) != n - 1:
            return False

        #build graph
        graph = defaultdict(list)
        q = deque()
        q.append(0)
        for a, b in edges:
            graph[b].append(a)
            graph[a].append(b)

        #check visited
        visited = set()
        visited.add(0)
        while q:
            node = q.popleft()
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)
        #return
        if len(visited) == n:
            return True
        else:
            return False




         
        