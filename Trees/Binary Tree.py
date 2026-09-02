#What is Binary Tree?
'''
A Binary Tree is a non linear data structure in which each node can have atmost two children
the two children are called:
*left child
*Right child
'''
#Example
'''       10
         /  \
        5    20
       / \    \
      3   7    30
      '''
#10 is root node
#5,20 children of 10
#3,7,30 leaf nodes
#note: binary does not mean every node must have exactly 2 children ,it means A node can have a maximum of 2 children

#Types of Binary trees
#1.Full Binary Tree:Every node has either 0 children,or 2 children
'''
       1
      / \
      2  3
     / \  
     4  5
no node has exactly one child
'''
#2.complete binary tree:all levels are completely filled except possibly the last level,and the
#last level is filled from left to right
'''
     1
    / \
    2  3
   / \ /
   4 5 6
heaps are implemented using complete binary trees  '''
#3.perfect binary tree:Every internal node has exactly two children and all leaf nodes are at the same level
'''     1
       / \
      2   3
     / \  / \
    4  5  6  7
for height h ,number of nodes is 2^(h+1)-1'''
#4.Balanced binary tree:the height of left and right subtrees is kept reasonably close
'''    10
      /  \
     5    20
    / \  /  \
   3  7 15   25
balanced trees helps maintain efficient operations
examples include:AVL tree,Red-Black Tree'''
#5.Degenerate/skewed binary tree:Each node has only one child
'''   10
       \
       20
        \
        30
         \
          40
it behaves almost like linked list
this can male operations O(n)'''




