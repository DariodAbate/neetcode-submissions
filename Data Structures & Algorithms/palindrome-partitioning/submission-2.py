class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []
        part = []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return 


            
            # check for every palindromic prefix of s[i:]
            for j in range(i, len(s)):
                if self.is_palindrome(s, i, j):
                    # at each step I can either choose to include s[i..j]
                    # or skip, to start a new partition
                    part.append(s[i:j + 1])
                    dfs(j + 1)

                    part.pop()
        dfs(0)
        return res
    
    def is_palindrome(self, s: str, start: int, end: int):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True