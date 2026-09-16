#Binary search tree:left<root<right
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def search(root,key):
    if root is None:
        return False
    if root.data==key:
        return True
    if key<root.data:
        return search(root.left,key)
    return search(root.right,key)
root=Node(50)
root.left=Node(30)
root.right=Node(70)
root.left.left=Node(10)
root.left.right=Node(40)
print(search(root,70))#True

#BST insertiom
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def insert(root,key):
    if root is None:
        return Node(key)
    if key<root.data:
        root.left=insert(root.left,key)
    elif key>root.data:
        root.right=insert(root.right,key)
    return root
root=Node(50)
root.left=Node(30)
root.right=Node(70)
root.left.left=Node(10)
root.left.right=Node(40)
root=insert(root,65)
print(root.right.left.data)#65
'''
Complexity
Balanced BST: O(log N)
Skewed BST: O(N)
Recursion space: O(H)'''

#BST Minimum:The minimum value is the leftmost node.
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def find_min(root):
    current=root
    while current.left:
        current=current.left
    return current
root=Node(50)
root.left=Node(30)
root.right=Node(70)
root.left.left=Node(10)
root.left.right=Node(40)
root=insert(root,65)
print(find_min(root).data)#10

#BST Maximum:Maximum = rightmost node.
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def find_max(root):
    current=root
    while current.right:
        current=current.right
    return current
root=Node(50)
root.left=Node(30)
root.right=Node(70)
root.left.left=Node(10)
root.left.right=Node(40)
root=insert(root,65)
print(find_max(root).data)#10