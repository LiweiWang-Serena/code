class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        merged = [0, 0, 0]

        for triplet in triplets:
            # 超标的triplet不能用, 直接跳过
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue

            # 安全的triplet, 把它合并(取max)进merged
            merged[0] = max(merged[0], triplet[0])
            merged[1] = max(merged[1], triplet[1])
            merged[2] = max(merged[2], triplet[2])

        return merged == target


            

        


        