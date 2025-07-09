# 169. Majority Element

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n= len(nums)//2 + 1
        return nums[n]
