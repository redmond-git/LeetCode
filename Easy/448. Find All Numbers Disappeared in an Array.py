from ast import main
from typing import List

class Solution:
    #time complexity: 
    #space complesity:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        result = []
        for n in nums:
            a = abs(n) - 1
            if nums[a] > 0: nums[a] *= -1

        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i+1)
        
        return result

        # return [i+1 for i in range(len(nums)) if nums[i] > 0]

        
nums = [4,3,2,7,8,2,3,1]
 
print(Solution.findDisappearedNumbers(main, nums))