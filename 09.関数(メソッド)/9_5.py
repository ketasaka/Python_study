def pu(m,n):
    a = m + n
    return a

def mi(m,n):
    b = m - n
    return b

def x(m,n):
    c = m * n
    return c

def par(m,n):
    d = int(m / n)
    return d

def ana(m,n):
    e = m % n
    return e

m = int(input("整数を入力してください："))
n = int(input("整数を入力してください："))
a = pu(m,n)
b = mi(m,n)
c = x(m,n)
d = par(m,n)
e = ana(m,n)
print(m,"+",n,"=",a,sep="")
print(m,"-",n,"=",b,sep="")
print(m,"*",n,"=",c,sep="")
print(m,"/",n,"=",d,sep="")
print(m,"%",n,"=",e,sep="")