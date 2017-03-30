class linkedList:
    def __init__(self,data):
        self.value = data
        self.next = None

class linkedListOperation:
    def insertEnd(self,head,key,value):
        if head.next != None:
            self.insertEnd(head.next,key,value)
        else:
            head.next = linkedList((key,value))

    def printList(self,head):
        if head.next is not None:
            print(head.value)
            self.printList(head.next)
        else:
            print(head.value)

    def delete(self, prev, head, key, value):
        if head != None:
            if head.value == (key,value) and prev == None:
                self.delete(None, head.next, key, value)
            elif head.value == (key,value):
                prev.next = head.next
            else:
                prev = head
                self.delete(prev, head.next, key, value)

class hashtable:
    def __init__(self,size):
        self.array = [None] * size
        self.size = size

    def hashFunction(self,size,key):
        return (key%size) # return the index to be inserted at

    def insertInto(self,key,value):
        index = self.hashFunction(self.size, key)
        # Check if collision at that location in array:
        if self.array[index] is None:
            self.array[index] = linkedList((key,value))
        else:
            insertLinked = linkedListOperation()
            insertLinked.insertEnd(self.array[index], key, value)

    def printTable(self):
        for intEntry,entry in enumerate(self.array):
            if entry is not None:
                print("@ Index %d " % intEntry)
                linkedListOperation().printList(entry)

def main():
    #linkedList
    head = linkedList((23,10))
    head.next = linkedList((24,11))
    head.next.next = linkedList((34,15))
    operation = linkedListOperation()
    operation.printList(head)
    print("\n\n---------------INSERT----------------")
    operation.insertEnd(head,1100,69)
    operation.printList(head)
    print("\n\n---------------DELETE 23,10 && 24,11----------------")
    operation.delete(None,head,23,10)
    operation.delete(None,head,24,11)
    operation.printList(head)

    print("\n\n\n---------------HASHTABLE----------------")
    #table
    table = hashtable(100)
    table.insertInto(239,"Hello")
    table.insertInto(139, "hello2")
    table.insertInto(112, "Inserted at 112 fam this is an entry")
    table.printTable()

if __name__ == '__main__':
    main()
