class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
    #    1 2 4 8
        def biggestBit(number,bit):
            if number>=2**(bit+1):
                return(biggestBit(number, bit+1))
            else:
                return(bit)
                
        def determineBinary(orig,binRep):
            if orig == 0:
                return binRep
            elif orig %2 ==1:
                binRep[-1]=1
                return(determineBinary(orig-1,binRep))
            else:
                temp = orig-(2**biggestBit(orig,0))
                index = biggestBit(orig,0)
                binRep[-index-1]=1
                return(determineBinary(temp,binRep))
          
        
        size = max(biggestBit(x,0),biggestBit(y,0))+1
        
        bitsX = [0]*size
        bitsY = [0]*size
        
        binX = determineBinary(x,bitsX)
        binY = determineBinary(y,bitsY)
        ham = 0
        print(binX,x,binY,y)
        for xElem,yElem in zip(binX,binY):
            if xElem != yElem:
                ham += 1
        return ham
                
