class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #return sorted(s) == sorted(t)
        #return Counter(s) == Counter(t)
       #first, because a set does not allow duplicate
       #we can use a set to get all unique carathare from string
       # then we accout the occurrency of each character in both string
       #if all character occur match, return true,else return false
        if len(s) != len(t):
            return False

        countS = {}
        countT = {}

        for i in range(len(s)):
            countS.setdefault(s[i], 0)
            countS[s[i]] += 1

            countT.setdefault(t[i], 0)
            countT[t[i]] += 1

        return countS == countT




        
        
