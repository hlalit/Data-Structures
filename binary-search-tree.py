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

    def remove(self, node):

        
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


