x = []
y = []
for i in range(3):
    x += [int(input("学生番号："))]
    y += [input("氏名：")]

for j in enumerate(x):
    print("学生番号：",x[j],"　氏名：",y[j])