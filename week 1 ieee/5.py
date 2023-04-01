def squaresum(k):
    sem=0
    for i in k:
        sem+=i**2
    return sem
amt=int(input('enter the number of elements you want to input into the list'))
lst=[]
for f in range(amt):
    num=int(input('enter element'))
    lst.append(num)
print(lst)
print(squaresum(lst))
    
        
