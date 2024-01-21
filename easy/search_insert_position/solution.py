from typing import List

class Solution:

    '''O(log(n))'''
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            half = (right + left) // 2 # cogemos la mitad (cociente entero)
            if nums[half] == target:
                return half
            elif target < nums[half]:
                right = half -1 # como la mitad es menor podemos poner que la derecha sea menor a la mitad
            else:
                left = half + 1 # como es mayor que el numero de la mitad pues podemos poner que la posicion de la izquierda sea mayor a la de la mitad
        return left

    ''' O(n)
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        finish = False
        while not finish:
            half = (right+left)// 2
            if target == nums[half]:
                return half
            elif target <= nums[left]:
                return left
            elif target > nums[right - 1]:
                return right
            left += 1
            right -= 1
    '''


    ''' O(n)
    def searchInsert(self, nums: List[int], target: int) -> int:
        num_lenght = len(nums)
        position = 0
        while target > nums[position]:
            if position == num_lenght - 1:
                return position + 1
            position += 1
        return position



    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        if target < nums[0]:
            return 0
        num_lenght = len(nums)
        if num_lenght == 1:
            return 1
        position = 1
        while target > nums[position]:
            if position == num_lenght - 1:
                return position + 1
            position += 1
        return position
    '''