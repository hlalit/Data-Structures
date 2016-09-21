class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

    def get_next(self,next):
        self.next = next
        return

class linked_list:
    size = int(0)

    def __init__(self):
        self.head = None

    def add(self,element):
        temp = Node(element)
        temp.get_next(self.head)
        self.head = temp
        return

    def traverse(self):

        current = self.head     #current is object of Node class
        while current != None:
            linked_list.size = linked_list.size + 1
            current = current.next

        print('Linked list has',linked_list.size,'nodes')
        return

    def insertion_sort(self):

        i = int(0)
        j = int(0)

        for i in range(1, linked_list.size): #number of passes required for insertion sort

            current = self.head
            next = current.next
            for j in range(0, linked_list.size - i): #number of comparisons per pass:

                if(current.val > next.val):
                    temp = current.val
                    current.val = next.val
                    next.val = temp

                current = current.next
                next = current.next

        ptr = self.head     #ptr is object of Node class: used to print the sorted list
        while ptr != None:
            print(ptr.val)
            ptr = ptr.next

        return

    def remove(self,index):
        counter = int(0)

        current = self.head
        while counter != index + 1:
            if(counter == index - 1):
                prev = current
                current = current.next
            elif(counter == index):
                prev.next = current.next
            else:
                current = current.next

            counter = counter + 1
        return

mylist = linked_list()
mylist.add(21)
mylist.add(32)
mylist.add(51)
mylist.add(64)
mylist.add(8)
mylist.add(34)
mylist.add(38)

mylist.traverse()

mylist.insertion_sort()

mylist.remove(2)






