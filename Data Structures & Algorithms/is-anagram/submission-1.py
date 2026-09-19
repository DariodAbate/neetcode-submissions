class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       # Ottimizzazione: se hanno lunghezze diverse, è impossibile che siano anagrammi
        if len(s) != len(t):
            return False
            
        s_chars, t_chars = {}, {}
        
        for i in range(len(s)):
            # dict.get(chiave, default) ti evita l'if iniziale!
            s_chars[s[i]] = s_chars.get(s[i], 0) + 1
            t_chars[t[i]] = t_chars.get(t[i], 0) + 1
            
        # Python sa confrontare due dizionari in automatico
        return s_chars == t_chars