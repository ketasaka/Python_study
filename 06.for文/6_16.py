sum = 0
for i in range(1,11):
    print(i,end="")
    n = int(input("回目の入力："))
    sum = sum + n
    if n == 0:
        print("0が入力されました。")
        break
    else:
        pass
print("合計：",sum)