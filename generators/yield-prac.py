
def squares(nums):
    for i in nums:
        yield (i*i)

a = [1,2,3,4,5]

ab = squares(a)

for each in ab:
    print (each)
