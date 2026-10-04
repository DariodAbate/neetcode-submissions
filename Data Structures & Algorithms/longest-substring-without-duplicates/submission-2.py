class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0 
        max_len = 0

        buffer = set()
        while r < len(s):
            if s[r] in buffer:
                while s[r] in buffer and l < r:
                    buffer.remove(s[l])
                    l += 1
            else:
                buffer.add(s[r])
                r += 1
                max_len = max(max_len, len(buffer))

        return max_len
