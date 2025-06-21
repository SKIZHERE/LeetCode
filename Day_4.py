# 14. Longest Common Prefix

class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        n = 0
        for i in range(len(strs[0])): 
            if strs[0][n] == strs[-1][n]:
                n += 1
            else:
                break
        return strs[0][:n]
