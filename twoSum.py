class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
      
        y = 0
        x = 1
       
        while y < len(nums)-1:
            while x < len(nums)-1:
                if nums[y] + nums[x] == target:
                    return y,x 
                else:
                    x +=1
           
                
            if nums[y] + nums[x] == target:
                return y,x 
          
              
            y +=1
            x = y+1
