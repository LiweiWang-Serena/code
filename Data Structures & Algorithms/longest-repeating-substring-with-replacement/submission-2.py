class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = defaultdict(int)
        l = 0
        maxC= 0
        for r, ch in enumerate(s):
            count[ch] += 1
            maxC = max(maxC, count[ch])
            
            while r - l + 1 - maxC > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res


        