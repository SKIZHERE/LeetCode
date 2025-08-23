# 268. Missing Number

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        nums.sort() #[0,1]
        if nums[-1] != len(nums): return len(nums)
        for i in range (len(nums)):
            if nums[i] != i: #0!=0, 1!=1
                return i
        """
        for i in range(len(nums)+1):
            if i not in nums:
                return i