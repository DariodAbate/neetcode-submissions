class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(" ", "")
        i = 0
        j = len(s) - 1

        while i < len(s)  and j >= 0:

            if not s[i].isalnum():
                i+=1
            elif not s[j].isalnum():
                j-=1
            elif s[i] == s[j]:
                i+=1
                j-=1
            else:
                return False

        return True
        