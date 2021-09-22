a = 0
b = 1
print(a,",",b,end="")
while True:
    c = a + b
    a = b
    b = c
    if b<=1000:
        print(",",b,end="")
    else:
        break