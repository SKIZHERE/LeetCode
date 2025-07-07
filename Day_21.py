# 125. Valid Palindrome

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_s = "".join(i for i in s.lower() if i.isalnum())
        if new_s[::-1] == new_s: return True
        return False