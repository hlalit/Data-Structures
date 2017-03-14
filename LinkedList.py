class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 
        
    def get_next(self,next):
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None 
        
    def create(self,val):
        temp = Node(val)
        temp.get_next(self.head)
        self.head = temp
        
    def writelist(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
            
    def reverselist(self): #the basic idea is that you need 3 pointers: current, prev (init:None) and next
        current = self.head
        prev = None 
        while current:
            next = current.next
            current.next = prev
            prev = current 
            current = next
        self.head = prev
        
    def insertk(self,val,pos):
        current = self.head
        prev = current
        temp = Node(val)
        
        index = 1
        if(pos > 1):
            while index != pos:
                prev = current
                current = current.next
                index = index + 1
            temp.next = current
            prev.next = temp
        else:
            temp.next = current
            self.head = temp
        
    def deletek(self,pos):
        current = self.head
        prev = current
        index = 1 
        
        if(pos > 1):
            while index != pos:
                prev = current
                current = current.next 
                index = index + 1
            prev.next = current.next 
        else:
            self.head = current.next
                                    
obj = LinkedList()
obj.create(4)
obj.create(9)
obj.create(2)
obj.create(3)
obj.create(5)
obj.create(7)
obj.create(8)
obj.writelist()
obj.reverselist()
print()
obj.writelist()
obj.insertk(10,2)
print()
obj.writelist()
print()
obj.deletek(2)
print()
obj.writelist()
