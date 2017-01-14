class Solution(object):
    def myAtoi(self, str):
        """:type str: str
        :rtype: int
        """
        buffer=" "
        isNeg = False
        isPos = False
        
        
        for numb, char in enumerate(str):
            if char == 0:
                continue
            elif char == "-":
                isNeg = True
                continue
            elif char == "+":
                isPos = True
                continue
            elif char == " " and numb == 0:
                continue
            
            try:
                int(char)
                buffer += char
                continue
            
            except ValueError:
                break
       
        try:
            if isNeg == False:
                return(int(buffer))
            elif isNeg == True and isPos == True:
                return (0)
            else:
                return(-(int(buffer)))
        except ValueError:
            return (0)
