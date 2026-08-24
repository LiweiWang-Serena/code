class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        
        for i, interval in enumerate(intervals):
            start, end = interval
            #newinterval in left
            if start > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]
            #new interval in right
            elif end < newInterval[0]:
                res.append(intervals[i])
                
            #new interval between
            else:
                newInterval = [min(intervals[i][0], newInterval[0]),
                max(intervals[i][1], newInterval[1])]
        res.append(newInterval)
        return res
            
                

            






