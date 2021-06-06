#difficulty = easy

class Solution:
    def twoSum(self, nums, target): 
        h = {}
        for i, num in enumerate(nums): # enumerate through the array
            n = target - num 
            if n not in h: 
                h[num] = i # append num to h ex: {0: 2, 1: 7}
            else:
                return [h[n], i] # return 
            
# reference HankLiu5 @ leetcode
