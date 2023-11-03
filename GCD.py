def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
i=int(input('Enter: '))
j=int(input('Enter: '))
if i<j:
    i,j=j,i
print(gcd(i,j))
