
# def squares(nums):
#     for i in nums:
#         yield (i*i)

a = [1,2,3,4,5]

# ab = [(each*each) for each in a]
#go from normal list comprehension to a generator by swapping out brackets with ()

ab = ((each*each) for each in a)

for each in ab:
    print (each)

# be careful casting contents of generator to a list, you loose efficiency of generator when doing this
