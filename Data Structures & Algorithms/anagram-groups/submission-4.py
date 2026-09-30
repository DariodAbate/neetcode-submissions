class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashes = {}
        for s in strs:
            hs = ''.join(sorted(s))
            if hs in hashes:
                hashes[hs].append(s)
            else:
                hashes[hs] = [s]

        return list(hashes.values())
