n=30
li=[]
for num in range(2,n+1):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        li.append(num)
print(li)
#[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

arr=[]
for num in range(2,n+1):
    prime=True
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            prime=False
            break
    if prime:
        arr.append(num)
print(arr)


    
    