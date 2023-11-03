d={}
a=input('Enter string: ')
for i in range(len(a)):
    if a[i] not in d:
        d.setdefault(a[i],0)
    else:
        d[a[i]]+=1
print(d)
