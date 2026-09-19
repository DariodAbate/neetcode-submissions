class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        s_chars, t_chars = {}, {}
        
        for i in range(len(s)):
            s_chars[s[i]] = s_chars.get(s[i], 0) + 1
            t_chars[t[i]] = t_chars.get(t[i], 0) + 1
            
        return s_chars == t_chars