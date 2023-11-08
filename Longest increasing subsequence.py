i=input('Enter values: ')
r=[int(x) for x in i.split()]
l=[1]*len(r)
for i in range(1,len(r)):
    for j in range(i):
        if r[j]<r[i] and l[i]<l[j]+1:
            l[i]=l[j]+1
print(max(l))
