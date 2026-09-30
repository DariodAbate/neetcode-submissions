class Solution:

    def encode(self, strs: List[str]) -> str:

        enc_str = ""
        for s in strs:
            enc_str += str(len(s)) + "-" + s

        return enc_str

    def decode(self, s: str) -> List[str]:
        dec_list = []

        i = 0
        while i < len(s):
            num = ""
            while s[i] != "-":
                num += s[i]
                i += 1
            i += 1 # skip the "-"

            nc = int(num)
            dec_list.append(s[i:i+nc])
            i += nc
            


        return dec_list
