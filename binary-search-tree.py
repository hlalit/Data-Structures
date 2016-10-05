class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class binary_search_tree:

    def __init__(self):
        self.root = None

    def create_tree(self, val, index):

        temp = Node(val)  #temp is object/pointer to Node class
        current = temp
        if(index == 0):
            self.root = current
        else:
            root = self.root
            while 1:
                if(current.value < root.value): #candidate for left subtree
                    next = root.left
                    if(next == None):
                        root.left = current
                        break

                    else:
                        root = root.left
                        continue

                if(current.value > root.value): #candidate for right subtree
                    next = root.right
                    if(next == None):
                        root.right = current
                        break

                    else:
                        root = root.right
                        continue
        return

    def inorder_traversal(self, node):

        if node.left:
            self.inorder_traversal(node.left)

        print(node.value)

        if node.right:
            self.inorder_traversal(node.right)

        return

    def preorder_traversal(self, node):

        print(node.value)

        if node.left:
            self.preorder_traversal(node.left)

        if node.right:
            self.preorder_traversal(node.right)
        return

    def postorder_traversal(self, node):

        if node.left:
            self.postorder_traversal(node.left)

        if node.right:
            self.postorder_traversal(node.right)

        print(node.value)


    def search(self, node, parent, item):

        if(node.value == item):         #node to delete does not have any children
            if(node.left == None and node.right == None):
                self.node = node
                self.parent = parent
                self.flag = 1

            elif(node.left == None and node.right != None):     #node to delete does not have a left child but a right child
                self.node = node
                self.parent = parent
                self.flag = 2

            elif(node.left != None and node.right == None):     #node to delete does not have a right child but a left child
                self.node = node
                self.parent = parent
                self.flag = 3

            elif(node.left != None and node.right != None):     #node to delete has both the left and right child
                self.node = node
                self.parent = parent
                self.flag = 4
        else:
            if node.left:
                self.search(node.left, node, item)

            if node.right:
                self.search(node.right, node, item)

            return

    def getMin(self, root):

        self.parent_of_min = self.node
        while 1:
            if root.left:
                self.parent_of_min = root
                root = root.left
                continue
            else:
                self.min = root
                break

    def remove(self, node):

        print("Enter element you want to remove: ")
        element = input()
        element = int(element)

        self.search(node, None, element)

        if (self.flag == 1):    #node to delete does not have any children
            if(self.node.value == self.parent.left.value):
                self.parent.left = None
            else:
                self.parent.right = None

        if(self.flag == 2):     #node to delete does not have a left child but a right child
            if(self.node.value == self.parent.left.value):
                self.parent.left = self.node.right
            else:
                self.parent.right = self.node.right

        if (self.flag == 3):    #node to delete does not have a right child but a left child
            if (self.node.value == self.parent.left.value):
                self.parent.left = self.node.left
            else:
                self.parent.right = self.node.left

        if(self.flag == 4):     #node to delete has both the left and right child
            self.getMin(self.node.right)        #finding minimum of the right subtree

            if(self.min.right == None):                             #if the minimum node has no right child
                if (self.node.value != self.parent_of_min.value):
                    self.parent_of_min.left = None
                    self.node.value = self.min.value

                if (self.node.value == self.parent_of_min.value):
                    self.node.right = None
                    self.node.value = self.min.value

            if(self.min.right != None):                               #if the minimum node has a right child still
                if(self.node.value != self.parent_of_min.value):
                    self.parent_of_min.left = self.min.right
                    self.node.value = self.min.value

                if(self.node.value == self.parent_of_min.value):
                    self.node.right = self.min.right
                    self.node.value = self.min.value

        return

tree = binary_search_tree() #tree is object of the binary_search_tree class
arr = [10, 5, 1, 7, 40, 50]

k = 0
for i in arr:
    tree.create_tree(i, k)
    k = k + 1

print("IMPLEMENTING DEPTH FIRST SEARCH ALGORITHMS FOR BINARY SEARCH TREES")
print("The In-order traversal of BST is: ")
tree.inorder_traversal(tree.root)
print("")
print("The Pre-order traversal of BST is: ")
tree.preorder_traversal(tree.root)
print("")
print("The Post-order traversal of BST is: ")
tree.postorder_traversal(tree.root)

tree.remove(tree.root)


