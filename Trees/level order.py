#level order Traversal:visiting the nodes of binary tree level by level,from left to right
#it is also called bfs
#example
'''
     10    <-level 0
    /  \
   20   30  <-level 1
  / \  /  \
40  50 60  70  <-level 2
level order visits:10->20->30->40->50->60->70
'''
#it uses queue that follow FIFO
'''
Steps:
Put the root (10) into the queue.
Remove 10 and print it.
Add its children (20, 30) to the queue.
Remove 20, print it, and add its children (40, 50).
Remove 30, print it, and add its children (60, 70).
Continue until the queue is empty.'''


class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
from collections import deque
def level_order(root):
    if root is None:
        return
    que=deque([root])
    while que:
        node=que.popleft()
        print(node.data,end=" ")
        if node.left:
            que.append(node.left)
        if node.right:
            que.append(node.right)
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(6)

level_order(root)
#1 2 3 4 5 6 6 
    
#DFS using stack
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def dfs(root):
    if root is None:
        return
    stack=[root]
    while stack:
        node=stack.pop()
        print(node.data,end=" " )
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(6)

dfs(root)
#1 2 4 5 3 6 6 