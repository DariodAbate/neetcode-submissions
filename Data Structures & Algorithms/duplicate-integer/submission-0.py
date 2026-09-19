class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasSeen = {}
        for el in nums:
            if el in hasSeen:
                return True
            else:
                hasSeen[el] = True
        return False