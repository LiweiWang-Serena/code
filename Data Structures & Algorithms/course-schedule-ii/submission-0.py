class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        q = deque()
        indegree = [0] * numCourses


        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)


        finished = 0
        order = []
        while q:
            course = q.popleft()
            finished += 1
            order.append(course)

            for nei in graph[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        if finished == numCourses:
            return order
        else:
            return []


        