f = open("hello.txt")
while True:
    line = f.readline()
    if not line:
        break
    print(line, end="")
f.close()


f = open("hello.txt")
line = f.read()
print(line, end="")
f.close()
