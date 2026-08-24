class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # 先按起始位置排序, 这样重叠的区间必然相邻
        intervals.sort(key=lambda x: x[0])

        res = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = res[-1][1]

            if start <= last_end:
                # 有重叠, 合并: 更新最后一个区间的结束点
                res[-1][1] = max(last_end, end)
            else:
                # 不重叠, 直接加进结果
                res.append([start, end])

        return res
        