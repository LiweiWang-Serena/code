class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            stone_x = heapq.heappop_max(stones)
            stone_y = heapq.heappop_max(stones)
            if stone_x < stone_y:
                heapq.heappush_max(stones, stone_y - stone_x)
        if len(stones) > 0:
            return stones[0]
        else:
            return 0



        