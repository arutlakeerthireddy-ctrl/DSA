#Linked list:
'''
A Linked list is a linear data structure in which elements(called Nodes) are connected using pointers.
unlike an array,linked list elements are not stored in contiguous memory
'''
#structure of Node:
'''
Each node contains
1.data:the values stored
2.next pointer:stores the address of the next node
+------+-------+   +------+------+
| Data |Next   |-->| Data | Next |
+------+-------+   +------+------+
#Example:10->20->30->Null'''

#Types
#1.Single Linked List
'''Each node points to the next node only
1->2->3->null
Traversal is only forward
simpler and uses less memory'''
#2.Double Linked list
'''
Each node has two pointers
*previous(prev)
*Next(next)
Null->1->2->3->Null
       <- <-
*can traverse forward and backward
*uses more memory
'''
#3.Circular Linked List
'''
The last node points back to the first node
1->2->3
|     |
-------
*No Null at the end
*useful for round-robin sheduling'''

#Advantages
'''
-Dynamic size
-Easy Insertion and deletion 
-Efficient memory usage when the size changes frequently
'''
#Disadvantages
'''
-Extra memory is needed for pointers
-slower access beacause elements must be traversed sequentially
-no direct indexing like arrays'''

#real world applications

#1.music playlist
'''
each node is a song
song1->song2->song3
next song -> move to the next node
previous song(using a doubly linked list)->move to the previous node'''
#2.web browser history
'''
a doubly linked list stores visited pages
google_->youtube_->github
back button->previous node
forward button->next node'''
#photo gallery
#round robin cpu scheduling(circular)
#undo/redo operations
#memory management
#GPS Navigation