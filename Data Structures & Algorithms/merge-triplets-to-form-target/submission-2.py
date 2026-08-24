class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        merge = [0, 0, 0]
        for trip in triplets:
            if trip[0] > target[0] or trip[1] > target[1] or trip[2] > target[2]:
                continue

            merge[0] = max(merge[0], trip[0])
            merge[1] = max(merge[1], trip[1])
            merge[2] = max(merge[2], trip[2])
        return merge == target
            

        


        