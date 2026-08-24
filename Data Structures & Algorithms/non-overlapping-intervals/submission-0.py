class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count = 0
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start < prev_end:
                # 重叠了, 必须删掉一个
                count += 1
                prev_end = min(prev_end, end)   # 贪心: 保留结束点更小的
            else:
                prev_end = end

        return count