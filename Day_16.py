# 83. Remove Duplicates from Sorted List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        obj = head
        while obj and obj.next:
            if obj.val == obj.next.val:
                obj.next = obj.next.next
            else:
                obj = obj.next
        return head