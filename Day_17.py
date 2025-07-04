# 88. Merge Sorted Array

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int  -- length nums1
        :type nums2: List[int]
        :type n: int  -- length nums2
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        nums1.sort()
