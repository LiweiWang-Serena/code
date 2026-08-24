import heapq

class MedianFinder:
    def __init__(self):
        self.left_maxheap = []
        self.right_minheap = []   
    def addNum(self, num):
        #put val to left first 
        #compare left and right val
        # compare to len left and right
        heapq.heappush(self.left_maxheap, -num)
        if (self.left_maxheap and self.right_minheap) and (-self.left_maxheap[0]) > self.right_minheap[0]:
            num = -heapq.heappop(self.left_maxheap)
            heapq.heappush(self.right_minheap, num)
        if len(self.left_maxheap) > len(self.right_minheap) + 1:
            num = -heapq.heappop(self.left_maxheap)
            heapq.heappush(self.right_minheap, num)
        if len(self.left_maxheap) + 1 < len(self.right_minheap):
            num = heapq.heappop(self.right_minheap)
            heapq.heappush(self.left_maxheap, -num)  
    def findMedian(self):
        if len(self.left_maxheap) > len(self.right_minheap):
            return -self.left_maxheap[0]
        if len(self.left_maxheap) < len(self.right_minheap):
            return self.right_minheap[0]
        return (-self.left_maxheap[0] + self.right_minheap[0]) / 2


       