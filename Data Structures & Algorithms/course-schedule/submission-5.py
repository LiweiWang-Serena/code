class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #topological sort
        #first build graph
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
        finished = 0
        while q:
            course = q.popleft()
            finished += 1
            for nei in graph[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        #return 
        if finished == numCourses:
            return True
        else:
            return False
        
        