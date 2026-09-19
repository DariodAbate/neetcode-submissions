class Solution:
    def mySort(self, elems: List[List[int]]):
        return elems[1]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1

        tuples = list(enumerate(nums))

        tuples.sort(key=self.mySort)

        while tuples[i][1] + tuples[j][1] != target:
            if tuples[i][1] + tuples[j][1] > target:
                j -= 1
            else:
                i += 1

        if tuples[i][0] < tuples[j][0]:
            return [tuples[i][0], tuples[j][0]]
        else :
            return [tuples[j][0], tuples[i][0]]
        