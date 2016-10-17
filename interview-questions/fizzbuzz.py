x = list(range(100))

for each in x:

    if each%3 == 0 and each%5 ==0:
        print("fizzbang")

    elif each % 3 == 0:
        print("fizz")

    elif each % 5 == 0:
        print("bang")
        
    else:
        print (each)
