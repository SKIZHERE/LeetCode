# 136. Single Number


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        print(nums)
        i = 0
        while i < len(nums)-1:
            if nums[i] != nums[i+1]:
                return nums[i]
            i = i+2
        return nums[-1]