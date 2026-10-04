class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0

        freqs = {} # ch -> freq_ch
        top_el = s[r]
        max_len = 0 

        while r < len(s):
            if s[r] not in freqs:
                freqs[s[r]] = 1
            else:
                freqs[s[r]] += 1
            top_el = self.update_top_el(freqs) 

            if r - l + 1 - freqs[top_el] > k:
                freqs[s[l]] = max(freqs[s[l]] - 1, 0)
                l += 1

            r += 1
            max_len = max(max_len,  r - l)
        
        return max_len
        
    def update_top_el(self, freqs: dict[str, int]) -> str:
        max_freq = 0
        top_el = "A"
        for el, fr in freqs.items():
            if max_freq < fr:
                max_freq = fr
                top_el = el
        return top_el

    

        