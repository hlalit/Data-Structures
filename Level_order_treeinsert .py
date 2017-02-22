class Node:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 
        
class LevelInsertTree:
    
    def __init__(self):
        self.head = None 
        self.l = l
        
    def insert(self,curr,val,arr,index):

        if(self.head == None):
            temp = Node(val)
            self.head = temp 
            current = temp
        else:
            current = curr
            
        left = 2*index + 1 
        right = 2*index + 2
        
        if(left > self.l or right > self.l):
            return
        
        if(left < self.l):
            leftnode = arr[2*index + 1]
            temp1 = Node(leftnode)
            current.left = temp1
        if(right < self.l):            
            rightnode = arr[2*index + 2]
            temp2 = Node(rightnode)
            current.right = temp2
        
        self.insert(temp1,leftnode,arr,left)
        self.insert(temp2,rightnode,arr,right)
        
    def inorder(self,current):
        if(current == None):
            return
        else:
            self.inorder(current.left)
            print(current.data)
            self.inorder(current.right)

arr = [3,1,2,4,5,6,9]
l = len(arr)
obj = LevelInsertTree()
obj.insert(obj.head,arr[0],arr,0)
obj.inorder(obj.head)
