class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #first we think about sort time complexity Olog(n)  
        hashMap = {}
        for i in nums:
            if i in hashMap:
               hashMap[i] += 1
            else:
                hashMap[i] = 1
        sorted_items = sorted(hashMap.items(), key = lambda x: x[1], reverse = True)
        result = [item[0] for item in sorted_items[:k]]
        return result

            
