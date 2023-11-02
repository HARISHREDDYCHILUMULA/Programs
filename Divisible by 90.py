ii=input('Enter values: ')

j=[int(x) for x in ii.split()]

count5,count0=0,0
for i in j:
    if i==5:
        count5+=1
    elif i==0:
        count0+=1
count5=(count5//9)*9
if count0==0:
    print('Nope')
elif count5==0:
    print('0')
else:
    print('5'*count5+'0'*count0)
