#1.Insert at position:Insert at a given index
#ex:Insert 25 at position 2
#Before:10->20->30->40
#After:10->20->25->30->40
#steps:
#1.reach previous node
#2.connect new node
# 3.update limks
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n1.next=n2
n2.next=n3
n3.next=n4
head=n1
print('Before Insertion:')
cur=head
while cur:
    print(cur.data,end='->')
    cur=cur.next
print("None")
new=Node(25)
new.next=n2.next
n2.next=new
print('After insertion:')
cur=head
while cur:
    print(cur.data,end='->')
    cur=cur.next
print('None')
'''
Before Insertion:
10->20->30->40->None
After insertion:
10->20->25->30->40->None'''
#or
#create a new node
#if position==1.insert at the beginning
#Traverse to the (position-1)th node
#update links
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n1.next=n2
n2.next=n3
n3.next=n4
head=n1
print("Before Insertion:")
cur=head
while cur:
    print(cur.data,end='->')
    cur=cur.next
print('None')
position=2
new=Node(25)
if position==1:
    new.next=head
    head=new
else:
    temp=head
    for i in range(position-1):
        temp=temp.next
    new.next=temp.next
    temp.next=new
print('After Insertion:')
cur=head
while cur:
    print(cur.data,end='->')
    cur=cur.next
print('None')

#1-based position-for i in range(position-2)
#0-based position-for i in range(postion-1)


