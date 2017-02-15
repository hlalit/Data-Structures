class Node:
    def __init__(self,data):
        self.data = data
        self.left = None 
        self.right = None

class BinaryTree:
    def __init__(self):
        self.head = None 

    def add(self,data):
        if(self.head == None):
            temp = Node(data)
            self.head = temp
        else:
            current= self.head
            temp = Node(data)
            while current:
                if(temp.data < current.data):
                    if(current.left == None):
                        current.left = temp
                        break
                    else:
                        current = current.left
                if(temp.data > current.data):
                    if(current.right == None):
                        current.right = temp
                        break
                    else:
                        current = current.right
                        
    def search(self,val):
        current = self.head 
        if(val == current.data):
            print("Found Data at Root Node")
            return 
        
        while current:
            if(val < current.data):
                current = current.left 
                continue
            if(val > current.data):
                current = current.right 
                continue
            if(val == current.data):
                print("Found Data")
                return 
        
        print("Could not find the node")
    
    def findmin(self,current):
            
        while current:
            parent = current
            current = current.left
            if(current == None):
                mininum = parent.data
                return mininum
        
    def delete(self,val):
        current = self.head
        
        if(val == current.data):
            return
        
        while current:
            if(val < current.data):
                parent = current
                current = current.left 
                continue 
            if(val > current.data):
                parent = current
                current = current.right 
                continue 
            if(val == current.data): #found the node to be deleted
                
                #case - 1 : when node to be deleted is leaf node
                if(current.left == None and current.right == None):
                    if(parent.left == current):
                        parent.left = None 
                    if(parent.right == current):
                        parent.right = None 
                        
                    print("node deleted !: node had no children")
                    return 
                 
                #case - 2 : when node to be deleted has one child
                if(current.left == None):
                    if(parent.left == current):
                        parent.left = current.right
                    if(parent.right == current):
                        parent.right = current.right
                    print("node deleted !: node had 1 right child")
                    return 
                
                if(current.right == None):
                    if(parent.left == current):
                        parent.left = current.left
                    if(parent.right == current):
                        parent.right = current.left                
                    print("node deleted !: node had 1 left child")
                    return 
                
                #case - 3 : when node to be deleted has two children
                if(current.left != None and current.right != None):
                    mininum = self.findmin(current.right)
                    print("The minimum is:", mininum)
                    self.delete(mininum)
                    current.data = mininum
                    print("node deleted !: node had 2 children")
                    return
            
    def inorder(self,current):
        if(current == None):
            return 
        else:
            self.inorder(current.left) 
            print(current.data)
            self.inorder(current.right)
            
        return 
    
    def preorder(self,current):
        if(current == None):
            return
        else:
            print(current.data)
            self.preorder(current.left)
            self.preorder(current.right)
            
    def postorder(self,current):
        if(current == None):
            return
        else:
            self.postorder(current.left)
            self.postorder(current.right)
            print(current.data)
                
            
obj = BinaryTree()
obj.add(10)
obj.add(20)
obj.add(5)
obj.add(15)
obj.add(30)
obj.add(25)
obj.add(40)
obj.add(7)
obj.search(30)
obj.delete(20)
obj.inorder(obj.head)
print()
obj.preorder(obj.head)
print()
obj.postorder(obj.head)

