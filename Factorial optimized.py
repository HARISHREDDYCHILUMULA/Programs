def fac(n,d={}):
    if n in d:
        return d[n]
    if n<=1:
        return 1
    d[n]=n*fac(n-1,d)
    return d[n]
print(fac(0))
