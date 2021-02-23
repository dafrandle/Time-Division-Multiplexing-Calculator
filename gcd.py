# written by NumWorks 3/04/2020
def gcd(a,b):
    while (b>0):
        r=a%b
        a,b=b,r
    return a