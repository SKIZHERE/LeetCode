# 58. Length of Last Word

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = s.split(" ")
        n = len(l)-1
        while n != 0:
            if l[n] == " ":
                n-=1
                print(l[n])
            else:
                return len(l[n])
