class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = {}
        l = 0
        maxC= 0
        for r, ch in enumerate(s):
            count[ch] += 1
            maxC = max(maxC, count[ch])
            win = r - l + 1
            while win - maxC > k:
                count[s[l]] -= 1
                l += 1
            if win - maxC <= k:
                res = max(res, r - l + 1)
        return res


        