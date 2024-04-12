def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

def lcm(a,b):
    return (a*b)//gcd(a,b)


def nu(num1,den1,num2,den2):
    
    common_denom=lcm(den1,den2)
    resnum1=num1*common_denom//den1
    resnum2=num2*common_denom//den2
    sumnum=resnum1+resnum2
    divisor=gcd(sumnum,common_denom)
    return sumnum//divisor, common_denom//divisor

d,e=nu(5,2,1,2)
print(d,' / ',e)
    
