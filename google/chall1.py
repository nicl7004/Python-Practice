
import re

def answer(s):
    normal = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    decyph = []
    input1 = list(s)
    for each in input1:
        if re.search('[\W]', each):
            decyph.append(each)
        elif each.isupper():
            newind =(normal.index(each.lower()))
            decyph.append(normal[newind].upper())
        elif re.search('[0-9]', each):
            decyph.append(each)
        else:
            index = normal.index(each)
            newind = 25 - index
            decyph.append(normal[newind])
    return(str(''.join(decyph)))
s = "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"

print (answer(s))
s = "wrw blf hvv ozhg mrtsg'h vkrhlwv?"
print(answer(s))
