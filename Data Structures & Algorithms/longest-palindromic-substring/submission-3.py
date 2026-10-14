class Solution:
    def longestPalindrome(self, s: str) -> str:
        lp = [0, 0]
        n = len(s)

        for center in range(n):
            # palindrome string can either have odd or evel length
            for start, end in [[center, center], [center, center + 1]]:
                left, right = self.expand(s, start, end)
                if right - left > lp[1] - lp[0]:
                    lp = [left, right]
        
        return s[lp[0]:lp[1]]

    def expand(self, s: str, start: int, end: int) -> [int]:
        while start >=0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
        return [start + 1, end] # adjust the bounds after last iteration

