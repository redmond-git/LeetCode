from ast import main
from typing import List

class Solution:
    #time complexity: 
    #space complesity:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (right + left) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
         
        return -1
 

        # left = 0
        # right = len(nums)-1
        
        # while left<=right:
        #     mid = (left+right)//2
        #     if nums[mid]==target:
        #         return mid
        #     elif nums[mid]>target:
        #         right = mid-1
        #     else:
        #         left = mid+1
        
        # return -1


nums = [-1,0,3,5,9,12]
target = 9

print(Solution.search(main, nums, target))