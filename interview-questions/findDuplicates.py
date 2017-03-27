
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        x = {}
        y = []
        for each in nums:
            if each in x:
                y.append(each)
                continue
            x[each] = x[each] +1
        return y
