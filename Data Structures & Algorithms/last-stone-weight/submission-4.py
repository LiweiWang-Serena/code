class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            stone_y, stone_x = heapq.heappop_max(stones), heapq.heappop_max(stones)
            if stone_x < stone_y:
                heapq.heappush_max(stones, stone_y - stone_x)
        return stones[0] if len(stones) > 0 else 0


        



        