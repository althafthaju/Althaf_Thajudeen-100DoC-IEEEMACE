def listenter(k):
    lst=[]
    for i in range(k):
        print('enter the element:',i,sep='')
        k=int(input())
        lst.append(k)
    sumf=0
    for i in lst:
        sumf+=i
    return lst,sumf
h=int(input('enter the total number of elements you want to add'))
print(listenter(h),sep='\n')
