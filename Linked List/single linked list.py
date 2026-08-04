#single linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
n1=Node(15)
n2=Node(10)
n3=Node(8)
n1.next=n2
n2.next=n3
head=n1
cur=head
while cur:
    print(cur.data,end="->")
    cur=cur.next
print('None')#15->10->8->None

#time complexity:O(n)
'''
create 3 nodes:O(1) for each node
connect nodes:O(1)
assign head and cur:O(1)
Traverse and print all nodes:O(n)'''
#space complexity:O(n)
#Auxiliary space complexity:O(1)

#Insertion at beginning:new node becomes the new head
'''
before
10->20->30
after inserting 5
5->10->20->30

#steps
# create new node
# point new node to current node
# update head'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
n1=Node(10)
n2=Node(20)
n3=Node(30)
n1.next=n2
n2.next=n3
head=n1
print("Before insertion:")
cur=head
while cur:
    print(cur.data,end="->")
    cur=cur.next
print('None')
new=Node(5)
new.next=head
head=new
print('After insertion:')
cur=head
while cur:
    print(cur.data,end="->")
    cur=cur.next
print("None")
'''
Before insertion:
10->20->30->None
After insertion:
5->10->20->30->None'''

#Insertion at end
'''
create a new node
if the list is empty,make the new node the head
traverse to the last node
set the last nodes next to the new node'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
n1=Node(10)
n2=Node(20)
n3=Node(30)
n1.next=n2
n2.next=n3
head=n1
print("Before Insertion:")
cur=head
while cur:
    print(cur.data,end="->")
    cur=cur.next
print('None')
new=Node(40)
temp=head
while temp.next:
    temp=temp.next
temp.next=new
print('After insertion:')
cur=head
while cur:
    print(cur.data,end="->")
    cur=cur.next
print('None')
'''
Before Insertion:
10->20->30->None
After insertion:
10->20->30->40->None'''