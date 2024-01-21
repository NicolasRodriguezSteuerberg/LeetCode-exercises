from typing import List

class Solution:

    '''Lento
    def removeDuplicates(self, nums: List[int]) -> int:
        dummy = []
        while nums:
            if nums[0] not in dummy:
                dummy.append(nums[0])
            nums.remove(nums[0])
        nums.extend(dummy)
        return len(nums)
    '''

    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count = 1
        for i in range(1, len(nums)):
            if(nums[i] != nums[i - 1]):
                nums[count] = nums[i]
                count+=1
        return count