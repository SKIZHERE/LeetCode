# 205. Isomorphic Strings

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                if d[s[i]] != t[i]:
                    return False
            d[s[i]] = t[i]
            if d.values().count(t[i]) > 1:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    s.isIsomorphic("badc", "baba")