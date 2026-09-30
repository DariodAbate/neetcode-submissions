class Solution:

    def encode(self, strs: List[str]) -> str:
        # the edge cases are [] and [""]. in the first case the output
        if not strs:
            return "@#@"

        return "#@#".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "@#@":
            return []

        strs = s.split("#@#")
        return strs
