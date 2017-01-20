import mem_profile
import random
import time

names = ['Nick', 'Mike', 'Gavin', 'Matt', 'Erik', 'Nick']
majors = ['Aerospace', 'Archie', 'Archie', 'mechanical', 'mechanical', 'comp sci']

print ('Memory before', mem_profile.memory_usage_resources(), "Mb")

def listRoommates(numberPpl):
    result = []
    for i in range(numberPpl):
        person = {
            'id' : i,
            'name' : random.choice(names),
            'major' : random.choice(majors)
        }

        result.append(person)
    return result

def generatorRoomate(numberPpl):
    for i in range(numberPpl):
        person = {
            'id' : i,
            'name' : random.choice(names),
            'major' : random.choice(majors)
        }

        yield person

t1 = time.clock()
people = listRoommates(1000000)
t2 = time.clock()

print("Memory after", mem_profile.memory_usage_resources(), "Mb\n")
print("Time used =", t2-t1, "seconds\n\n")
