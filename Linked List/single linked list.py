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