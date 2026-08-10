#priority-process the element according to its priority
#heap-a data structure commonly used to inplement a priority queue efficient
import heapq
a=[]
heapq.heappush(a,10)
heapq.heappush(a,5)
heapq.heappush(a,20)
heapq.heappush(a,2)
heapq.heappush(a,8)
print(a)#[2, 5, 20, 10, 8]
print(a[0])#2
#parent<=child nodes

import heapq
num=[10,5,20,2,8]
heapq.heapify(num)
print(num)#[2, 5, 20, 10, 8]



