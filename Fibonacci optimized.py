def fib(n,d={}):
    if n in d:
        return d[n]
    if n<=1:
        return n
    d[n]=fib(n-1,d)+fib(n-2,d)
    return d[n]
print([fib(i) for i in range(6)])
