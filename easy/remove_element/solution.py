from typing import List

class Solution:
    '''Rendimientos similares, esta es más facil entender y de leer'''
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        return count

    '''Rendimiento similar
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] == val:
                nums[left] = nums [right]
                right -= 1
            else:
                left += 1
    '''


    '''Recordando métodos de borrado, poco efectivo si son muchos elementos
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums),0,-1): # we go from last to the first we could do this also: for i in range(len(nums))[::-1]
            if nums[i]==val:
                nums.pop(i) # eliminamos
        return len(nums)

    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)
    '''