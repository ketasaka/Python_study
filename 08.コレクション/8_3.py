x = []
y = []
for i in range(10):
    a = int(input("{}件目：整数値を入力　＝".format(i + 1)))
    if a % 2 == 0:
        x += [a]
    else :
        y += [a]
print("偶数値リスト＝",x)
print("奇数値リスト",y)