from ast import main
from typing import List

class Solution:
    #time complexity: 
    #space complesity:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []

        result = [[0] * n for _ in range(m)]
        idx = 0

        for i in range(m):
            for j in range(n):
                result[i][j] = original[idx]
                idx += 1

        return result
 

original = [1,2,3]
m = 1
n = 3
print(Solution.construct2DArray(main, original, m, n))