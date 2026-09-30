class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {} # if no key, insert it with value 1
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        keys = []
        for key in sorted(freq, key=freq.get, reverse=True):
            keys.append(key)

        return keys[0:k]
             
