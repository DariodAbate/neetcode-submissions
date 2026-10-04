class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0

        freqs = {} # ch -> freq_ch
        max_f = 0
        max_len = 0 

        while r < len(s):
            if s[r] not in freqs:
                freqs[s[r]] = 1
            else:
                freqs[s[r]] += 1
            
            max_f = max(max_f, freqs[s[r]])

            if r - l + 1 - max_f > k:
                freqs[s[l]] = freqs[s[l]] - 1
                l += 1

            r += 1
            max_len = max(max_len,  r - l)
        
        return max_len
        