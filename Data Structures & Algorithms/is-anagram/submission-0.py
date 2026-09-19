class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = {}
        t_chars = {}
        for ch in s:
            if ch not in s_chars:
                s_chars[ch] = 0
            s_chars[ch] = s_chars[ch] + 1

        for ch in t:
            if ch not in t_chars:
                t_chars[ch] = 0
            t_chars[ch] = t_chars[ch] + 1

        if len(s_chars) != len(t_chars):
            return False;
        
        for k, v in s_chars.items():
            if k not in t_chars or t_chars[k] != v:
                return False
        return True