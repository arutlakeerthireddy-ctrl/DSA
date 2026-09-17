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
print(search(root,70))#TrueS
    
    
        
        
