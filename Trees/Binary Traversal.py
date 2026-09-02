#Binary Tree
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
root=Node(10)
root.left=Node(20)
root.right=Node(30)
print(root.data)
print(root.left.data)
print(root.right.data)

#Traversing:visiting every node of the tree
#1.preorder
#root->left->right
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def preorder(node,res):
    if not node:
            return
    res.append(node.data)#root
    preorder(node.left,res)
    preorder(node.right,res)
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.right=Node(6)
res=[]
preorder(root,res)
print(*res)
#1 2 4 5 3 6

#inorder
#left->root->right
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def inorder(node,res):
    if not node:
        return
    inorder(node.left,res)
    res.append(node.data)
    inorder(node.right,res)
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(6)
res=[]
inorder(root,res)
print(*res)
#4 2 5 1 6 3 6

#postorder
#left->right->root
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def postorder(node,res):
    if not node:
        return
    postorder(node.left,res)
    postorder(node.right,res)
    res.append(node.data)
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(6)
res=[]
postorder(root,res)
print(*res)
#4 5 2 6 6 3 1
        