##ls = [sun, mon, tue, wed, thur, fri, sat]
#mon, 2
#output= wed

#frid, 2000
#output: tue
'''
li=['sun', 'mon', 'tue', 'wed', 'thur', 'fri', 'sat']
a=input()
num=int(input())
for i in range(len(li)):
    if li[i]==a:
        print(li[(i+num)%len(li)])

'''

#binary tree
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
root=Node(10)
root.left=Node(5)
root.right=Node(15)
root.left.left=Node(2)
root.left.right=Node(7)
print(root.data)
print(root.left.data)
print(root.right.data)
print(root.left.left.data)
print(root.left.right.data)

#preorder
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def preorder(root):
    if root is None:
        return
    print(root.data,end=" ")
    preorder(root.left)
    preorder(root.right)
root=Node(10)
root.left=Node(5)
root.right=Node(15)
root.left.left=Node(2)
root.left.right=Node(7)
preorder(root)#10 5 2 7 15 
    
