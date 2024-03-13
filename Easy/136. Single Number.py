from ast import main
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numset = set()

        for x in nums:
            if x in numset:
                numset.remove(x)
            else:
                numset.add(x)

        return numset.pop()
    
    
nums = [4,1,2,1,2]
print(Solution.singleNumber(main, nums))