class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        merge = [0, 0, 0]
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            merge[0] = max(merge[0], t[0])
            merge[1] = max(merge[1], t[1])
            merge[2] = max(merge[2], t[2])
        return merge == target
            

        


        