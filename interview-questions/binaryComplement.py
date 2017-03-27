class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        #get binary rep
            #16 8 4 2 1
        def getBiggest(number,bit):
            if number >= 2**(bit+1):
                return(getBiggest(number, bit+1))
            else:
                return(bit)
                
        def getBinary(number,listB):
            if number ==0:
                return(listB)
            elif number %2 ==1:
                listB[-1] = 1
                return(getBinary(number,listB))
            else:
                newNumb = number - 2**getBiggest(number,0)
                newBit = getBiggest(number,0)
                return(getBinary(newNumb,listB))
            
        
       
                
        #add one to the largest bit
        size = [0]*(getBiggest(num,0)+1)
        binRep = getBinary(num,size)
        
        complement = [None]*len(binRep)
        
        for inteach, each in enumerate(binRep):
            if each == 1:
                complement[inteach] = 0
            else:
                complement[inteach] = 1
        
        print(complement)
        
                
