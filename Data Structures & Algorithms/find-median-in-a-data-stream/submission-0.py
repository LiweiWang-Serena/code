import heapq

class MedianFinder:
    def __init__(self):
        self.maxheap_left = []    # 左半边(较小的一半),最大堆,存负数模拟
        self.minheap_right = []   # 右半边(较大的一半),最小堆

    def addNum(self, num):
        # 1. 先丢进左半边(最大堆,存负数)
        heapq.heappush(self.maxheap_left, -num)

        # 2. 保证左边最大 ≤ 右边最小,否则把左堆顶挪到右边
        if (self.maxheap_left and self.minheap_right and
                (-self.maxheap_left[0]) > self.minheap_right[0]):
            val = -heapq.heappop(self.maxheap_left)
            heapq.heappush(self.minheap_right, val)

        # 3. 平衡两堆大小,差不超过 1
        if len(self.maxheap_left) > len(self.minheap_right) + 1:
            val = -heapq.heappop(self.maxheap_left)
            heapq.heappush(self.minheap_right, val)
        if len(self.minheap_right) > len(self.maxheap_left) + 1:
            val = heapq.heappop(self.minheap_right)
            heapq.heappush(self.maxheap_left, -val)

    def findMedian(self):
        if len(self.maxheap_left) > len(self.minheap_right):
            return -self.maxheap_left[0]                       # 左边多一个,取左堆顶
        if len(self.minheap_right) > len(self.maxheap_left):
            return self.minheap_right[0]                       # 右边多一个,取右堆顶
        return (-self.maxheap_left[0] + self.minheap_right[0]) / 2   # 一样多,取两堆顶平均
        