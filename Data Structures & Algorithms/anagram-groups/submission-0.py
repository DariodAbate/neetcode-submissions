class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashes = {}
        for s in strs:
            hs = hash(''.join(sorted(s)))
            if hs in hashes:
                elems = hashes.get(hs)
                elems.append(s)
                hashes[hs] = elems
            else:
                hashes[hs] = [s]

        out = []
        for k, v in hashes.items():
            out.append(v)
        return out
