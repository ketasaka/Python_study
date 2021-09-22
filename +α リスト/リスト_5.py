x = []

x = [225,13,50,1002,133,99,]
print(sorted(x))

print(x[2:6])

x[2:6] = [10,10,10,10]
print(x)
y = [777,888,999]
x += y
print(x)
print(len(x))
x.insert(7,117)
print(x)
x.remove(117)
print(x)
x = []
print(x)
del x
print(x)
