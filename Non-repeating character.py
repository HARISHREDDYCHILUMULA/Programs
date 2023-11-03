d={}
a=input('Enter string: ')
for i in range(len(a)):
    if a[i] not in d:
        d.setdefault(a[i],0)
    else:
        d[a[i]]+=1
for i,j in d.items():
    if j==0:
        print(i)
