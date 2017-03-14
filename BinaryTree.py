class Node:
    def __init__(self,data):
        self.data = data
        self.left = None 
        self.right = None 
        
class Tree:
    def __init__(self):
        self.head = None 
        self.list = []
        
    def push(self,data):
        
        self.list.append(data)
        return
    
    def insertTree(self,data,address,index):
        
        if(self.head == None):
            temp = Node(data)
            current = temp
            self.head = current
        else:
            current = address
        
        lindex = 2*index + 1
        rindex = 2*index + 2
        
        if(lindex < len(self.list)):
            lnode = Node(self.list[lindex])
            left = self.list[lindex]
            current.left = lnode
            self.insertTree(left,lnode,lindex)
        else:
            return
        
        if(rindex < len(self.list)):
            rnode = Node(self.list[rindex])
            right = self.list[rindex]
            current.right = rnode
            self.insertTree(right,rnode,rindex)
        else:
            return
        
    def inorder(self,current):
        if(current == None):
            return 
        else:
            self.inorder(current.left)
            print(current.data)
            self.inorder(current.right)
            
    def levelorder(self,current):
        if(current == None):
            return
        q = []
        q.append(current)
            
        while len(q) > 0:
            print(q[0].data)
            node = q.pop(0)
            
            if(node.left):
                q.append(node.left)
            if(node.right):
                q.append(node.right)
                
    def height(self,current):
        if(current == None):
            return -1
        else:
            lheight = self.height(current.left)
            rheight = self.height(current.right)
            
            if(lheight > rheight):
                return lheight + 1
            else:
                return rheight + 1 
                            
obj = Tree()
obj.push(2)
obj.push(3)
obj.push(5)
obj.push(7)
obj.push(1)
obj.push(10)
obj.push(9)
obj.push(8)
obj.insertTree(obj.list[0],obj.head,0)
obj.inorder(obj.head)
print()
obj.levelorder(obj.head)
print()
obj.height(obj.head)
print()
