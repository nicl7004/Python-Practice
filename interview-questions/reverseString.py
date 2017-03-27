class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        x = []
        
        y = len(s) -1
        s = list(s)
        while y >= 0:
            x.append(s[y])
           
            y -=1
        return "".join(x)
