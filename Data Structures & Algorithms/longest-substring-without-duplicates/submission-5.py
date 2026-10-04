class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0 
        max_len = 0

        buffer = set()
        while r < len(s):
            while s[r] in buffer:
                buffer.remove(s[l])
                l += 1

            buffer.add(s[r])
            r += 1
            max_len = max(max_len, len(buffer))

        return max_len
