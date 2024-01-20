from typing import List

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ''' Brute force mode, not recomended
        for i in range(0,len(nums)): # we dont use len - 1 because range dont go to the last number
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    nums2 = [i,j]
                    return nums2
        '''

        ''' Con hash tables (bastante mas eficiente)'''
        numMap = {} # this is gona be a dictionary
        for i in range(len(nums)):
            complement = target - nums[i]
            if (complement in numMap): # this search if exists the key (complement) in the ditionary
                return [i, numMap[complement]] # return position i and position in numMap which key is the complement
                # if you use a return statement, it'll skip the rest and immediately return the specified value
            numMap[nums[i]] = i # we add another element to the dictionary
            # to add an element in a dictionary, you need to put the key in [] and assign it a value
        return [] # if a solution is not found