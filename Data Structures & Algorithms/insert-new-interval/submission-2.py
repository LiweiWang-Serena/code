class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        start = 0
        end = 1
        for i in range(len(intervals)):
            #newinterval in left
            if intervals[i][0] > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]
            #new interval in right
            elif intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
                
            #new interval between
            else:
                newInterval = [min(intervals[i][0], newInterval[0]),
                max(intervals[i][1], newInterval[1])]
        res.append(newInterval)
        return res
            
                

            






