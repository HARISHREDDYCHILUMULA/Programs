def perfect_number(n):
    b=0
    for i in range(1,n):
        if n%i==0:
            b+=i
    if b==n:
        print('Perfect Number')
    else:
        print('Not a perfect number')
perfect_number(int(input('Enter number: ')))
