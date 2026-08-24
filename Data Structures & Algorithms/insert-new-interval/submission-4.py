class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #data structure list
        #algorithm greedy
        res = []
        #interval in left
        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]
        #interval in right
            elif intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
        #interval between
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
        res.append(newInterval)
        return res
        #time complexity O(n) space complexity O(n)



                
            
                

            






