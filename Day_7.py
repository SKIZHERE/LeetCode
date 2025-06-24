# 26. Remove Duplicates from Sorted Array

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = 0
        for i in range(1,len(nums)):
            if nums[n] != nums[i]:
                n+=1
                nums[n] = nums[i]
        return n+1
