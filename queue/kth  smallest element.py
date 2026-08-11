#kth smallest element in an array
import heapq
nums=list(map(int,input().split()))
k=2
heap=[]
for i in nums:
    heapq.heappush(heap,-i)
    if len(heap)>k:
        heapq.heappop(heap)
print(-heap[0])
