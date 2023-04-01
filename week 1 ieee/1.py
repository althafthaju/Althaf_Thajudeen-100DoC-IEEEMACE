a=input('enter the string')
h=''
for k in a:
    if ord(k)in range(65,91):
        h+=k
    if ord(k) in range(97,123):
        h+=k
print(h)
for k in h:
    if ord(k)in range(65,91):
        print(str(ord(k)-64),end=' ')
    elif ord(k) in range(97,123):
        print(str(ord(k)-96),end=' ')
