class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        q = deque()
        indgree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indgree[course] += 1

        #indegree 0
        for course in range(numCourses):
            if indgree[course] == 0:
                q.append(course)


        #indegree nei
        finished = 0
        while q:
            course = q.popleft()
            finished += 1
    
            for nei in  graph[course]:
                indgree[nei] -= 1
                if indgree[nei] == 0:
                    q.append(nei)

        if finished == numCourses:
            return True
        else:
            return False

        

        

            



        
        