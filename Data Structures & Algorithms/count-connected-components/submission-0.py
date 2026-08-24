class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        q = deque()
        q.append(0)
        for a, b in edges:
            graph[b].append(a)
            graph[a].append(b)

        visited = set()
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                
            q = deque()
            q.append(i)
            visited.add(i)   
            while q:
               node = q.popleft()
               for nei in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
        
        
        return count


        