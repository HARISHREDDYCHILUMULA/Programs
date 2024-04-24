n=int(input('Enter number for sqrt'))
def sq(n):
    i=1
    while True:
        if i*i==n:
            return i
        elif i*i>n:
            d=calc(n,i-1,i)
            return d
        i+=1
def calc(n,i,j):
    while abs(i-j)>0.000005:
        mi=(i+j)/2
        mid=mi*mi
        if mid==n:
            return mid
        elif mid<n:
            i=mi
        else:
            j=mi
    return (i+j)/2
print(sq(n))
