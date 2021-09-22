def zibunn15():
    print("合計点と平均点を求めます。")
    m = int(input("学生の人数："))
    sum = 0
    for i in range(m):
        print(i+1,end="")
        n = int(input("番目の点数："))
        sum = sum + n
    ave = sum / m
    print("合計は",sum,"点です。")
    print("平均は",ave,"点です。")

def kaitou15():
    print("合計点と平均点を求めます。")
    m = int(input("学生の人数："))
    n = [None] * m
    for i in range(m):
        n[i] = int(input("{}番目の点数：".format(i+1)))
    total = 0
    for i in range(m):
        total += n[i]
    ave = total / m
    print("合計は",total,"点です。")
    print("平均は",ave,"点です。") 


print("合計点と平均点を求めます。")
n = []
m = 0
while True:
    k = input("{}番目の点数：".format(m+1))
    if k == "end":
        break
    n.append(int(k))
    m += 1
total = sum(n)
print("合計は",total,"点です。")
print("平均は",total/m,"点です。") 