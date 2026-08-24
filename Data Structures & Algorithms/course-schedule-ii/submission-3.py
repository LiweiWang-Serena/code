class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #build graph
        graph = defaultdict(list)
        q = deque()
        indegree = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        #indegree 0
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        #indegree nei
        order = []
        while q:
            course = q.popleft()
            order.append(course)

            for nei in graph[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        #return
        if len(order) == numCourses:
            return order
        else:
            return []
        
        