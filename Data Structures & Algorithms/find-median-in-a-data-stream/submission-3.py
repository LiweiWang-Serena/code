import heapq

class MedianFinder:
    def __init__(self):
        self.left_maxheap = []
        self.right_minheap = []
    def addNum(self, num):
        #put left num in heap
        heapq.heappush(self.left_maxheap, -num)
        #make sure left num < right num
        if (self.left_maxheap and self.right_minheap) and (-self.left_maxheap[0]) > (self.right_minheap[0]):
            val = -heapq.heappop(self.left_maxheap)
            heapq.heappush(self.right_minheap, val)
        #make sure left count and right count diff not more than 1
        #if len left > len right +1 pop left push to right
        if len(self.left_maxheap) > len(self.right_minheap) + 1:
            val = -heapq.heappop(self.left_maxheap)
            heapq.heappush(self.right_minheap, val)
        if len(self.right_minheap) > len(self.left_maxheap) + 1:
            val = heapq.heappop(self.right_minheap)
            heapq.heappush(self.left_maxheap, -val)
    def findMedian(self):
        if len(self.left_maxheap) > len(self.right_minheap):
            return -self.left_maxheap[0]
        if len(self.right_minheap) > len(self.left_maxheap):
            return self.right_minheap[0]
        
        return (-self.left_maxheap[0] + self.right_minheap[0]) / 2

        

       