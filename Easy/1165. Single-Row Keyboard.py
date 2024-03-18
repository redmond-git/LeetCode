from ast import main
from typing import List

class Solution:
    #time complexity: 
    #space complesity:
    def calculateTime(self, keyboard: str, word: str) -> int:
        keys = {}
        for i, k in enumerate(keyboard):
            keys[k] = i
        
        time_moves = 0
        current_ind = 0
        for k in word:
            time_moves += abs(keys[k] - current_ind)
            current_ind = keys[k]

        return time_moves

keyboard = "pqrstuvwxyzabcdefghijklmnop"
word = "leetcode"
print(Solution.calculateTime(main, keyboard, word))