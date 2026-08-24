class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #return sorted(s) == sorted(t)
        #return Counter(s) == Counter(t)
       #first, because a set does not allow duplicate
       #we can use a set to get all unique carathare from string
       # then we accout the occurrency of each character in both string
       #if all character occur match, return true,else return false
        set_ = set(s)
        if len(s) != len(t):
            return False
        for i in set_:
            if s.count(i) != t.count(i):
                return False
        else:
            return True

