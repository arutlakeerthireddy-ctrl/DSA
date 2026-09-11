##ls = [sun, mon, tue, wed, thur, fri, sat]
#mon, 2
#output= wed

#frid, 2000
#output: tue
li=['sun', 'mon', 'tue', 'wed', 'thur', 'fri', 'sat']
a=input()
num=int(input())
for i in range(len(li)):
    if li[i]==a:
        print(li[(i+num)%len(li)])

    


