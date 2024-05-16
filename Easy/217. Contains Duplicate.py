from ast import main
from typing import List

class Solution:
    #time complexity: 
    #space complesity:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = set()

        for i in nums:
            
            if i in d:
                return True
            else:
                d.add(i)

        return False


nums = [1,1,1,3,3,4,3,2,4,2]
 
print(Solution.containsDuplicate(main, nums))