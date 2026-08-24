from typing import List
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 1. 统计每个任务出现次数
        count = Counter(tasks)

        # 2. 找最大次数 maxf
        maxf = 0
        for v in count.values():
            if v > maxf:
                maxf = v

        # 3. 数有几个任务并列最多 maxc
        maxc = 0
        for v in count.values():
            if v == maxf:
                maxc += 1

        # 4. 套公式算骨架长度
        skeleton = (maxf - 1) * (n + 1) + maxc

        # 5. 和任务总数取大值(防止洞被填爆)
        return max(len(tasks), skeleton)