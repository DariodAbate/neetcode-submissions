class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)

        max_seq = 0
        for num in nums:
            if num - 1 not in hs:
                # start searching for the longest sequence
                prox = num + 1
                seq = 1
                while prox in hs:
                    seq += 1
                    prox += 1
                max_seq = max(seq, max_seq)
        
        return max_seq

            


        