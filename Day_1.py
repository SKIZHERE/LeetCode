class Solution(object):

    def twoSum(self, nums, target):
        for n1,i in enumerate(nums):
            for n2,j in enumerate(nums):
                if n1 != n2 and i+j == target:
                    return n1,n2