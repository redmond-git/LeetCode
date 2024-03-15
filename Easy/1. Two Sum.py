from ast import main
from typing import List

class Solution:
    #time complexity: 
    #space complesity:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        delta = {}

        for i, j in enumerate(nums):
            r = target - j

            if r in delta:
                return [delta[r], i]
            else:
                delta[j] = i

        return []


nums = [2,7,11,15]
target = 9
print(Solution.twoSum(main, nums, target))