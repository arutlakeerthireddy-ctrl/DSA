#1.Basic queue using an array and two pointers
queue=[None]*5
front=0
rear=-1
#Enqueue 10
rear+=1
queue[rear]=10
#Enqueue 20
rear+=1
queue[rear]=20
#Enqueue 30
rear+=1
queue[rear]=30
print(queue)
#dequeue
print('Removed:',queue[front])
front+=1
print('Removed:',queue[front])
front+=1
'''
[10, 20, 30, None, None]
Removed: 10
Removed: 20'''

#we can say queue is empty if front>rear