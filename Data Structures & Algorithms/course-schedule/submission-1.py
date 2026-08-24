class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #build graph 
        graph = defaultdict(list) #default dict for new dict without key
        q = deque() #initial q for toplogical
        indgree = [0] * numCourses #initial indgree to find out rely

        #algorithm function
        for course, pre in prerequisites:
            graph[pre].append(course)
            indgree[course] += 1

        #first to caculate without rely    
        for i in range(numCourses):
            if indgree[i] == 0:
                q.append(i)


        #second to caulate rely relationship neighbour
        finished = 0
        while q:
            course = q.popleft()
            finished += 1

            for nei in graph[course]:
                indgree[nei] -= 1
                if indgree[nei] == 0:
                    q.append(nei)


        #main function
        if finished == numCourses:
            return True
        else:
            return False


        

        

            



        
        