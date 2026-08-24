class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        merged = [0, 0, 0]
        for trip in triplets:
            if trip[0] > target[0] or trip[1] > target[1] or trip[2] > target[2]:
                continue
            merged[0] = max(merged[0], trip[0])
            merged[1] = max(merged[1], trip[1])
            merged[2] = max(merged[2], trip[2])
        return merged == target
            

            

        


        