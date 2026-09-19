class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1

        tuples = []
        for idx, num in enumerate(nums):
            tuples.append([idx, num])
        tuples.sort(key=lambda x: x[1])

        while tuples[i][1] + tuples[j][1] != target:
            if tuples[i][1] + tuples[j][1] > target:
                j -= 1
            else:
                i += 1

        if tuples[i][0] < tuples[j][0]:
            return [tuples[i][0], tuples[j][0]]
        else :
            return [tuples[j][0], tuples[i][0]]
        