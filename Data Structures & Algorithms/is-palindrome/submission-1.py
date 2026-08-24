class Solution:
    def isPalindrome(self, s: str) -> bool:
        #we use two pointer, left and right
        s_1 = ""
        for i in s:
            if i.isalnum():
                s_1 += i.lower()
        return s_1 == s_1[::-1]