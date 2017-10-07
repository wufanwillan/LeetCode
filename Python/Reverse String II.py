# Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
# Example:
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# Restrictions:
# The string consists of lower English letters only.
# Length of the given string and k will in the range [1, 10000]

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ls=len(s)
        base=0
        result=[]
        listr=[]
        s=list(s)
        while base+2*k<=ls:
            listr=s[base:base+k]
            listr.reverse()
            result.extend(listr)
            result.extend(s[base+k:base+2*k])
            base+=2*k
        if base+k<=ls:
            listr=s[base:base+k]
            listr.reverse()
            result.extend(listr)
            result.extend(s[base+k:])
        else:
            listr=s[base:]
            listr.reverse()
            result.extend(listr)
        return ''.join(result)
