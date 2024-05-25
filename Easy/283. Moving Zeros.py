from ast import main
from typing import List

class Solution:
    #time complexity: 
    #space complesity:
    def moveZeroes(self, nums: List[int]) -> None:
        
        z = 0
         
        for i in range(len(nums)):
            if nums[i] != 0 and nums[z] == 0:
                nums[z], nums[i] = nums[i], nums[z]
                z += 1
            elif nums[i] != 0 and nums[z] != 0:
                z += 1

        pass

    def moveZeroes2(self, nums: List[int]) -> None:
        anchor = 0
        for explorer in range(len(nums)):
            if nums[explorer] != 0:
                nums[anchor], nums[explorer] = nums[explorer], nums[anchor]
                anchor += 1
                

        pass


nums = [0,0,0,0,0]
 

print(Solution.moveZeroes(main, nums))