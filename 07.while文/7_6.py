a = 0
n = 0
sum = 0
while True:
    a = int(input("整数を入力："))
    if a == 0:
        break
    else :
        sum += a
        n += 1
if sum == 0:
    ave = 0
else :
    ave = sum/n
print("合計値：",sum)
print("平均値",ave)