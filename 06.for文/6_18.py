print("カレンダーを表示させます。")
print("0:日 1:月 2:火 3:水 4:木 5:金 6:土")
m = int(input("表示させたい月は何曜日から始まりますか："))
n = int(input("表示させたい月は何日ありますか："))
day = 1
o = m
print(" 日 月 火 水 木 金 土")
for i in range(1,n + 1):
    if o != 0:
        for j in range(1,o+1):
            print("   ",end="")
        o = 0
    else:
        pass
    if (i - 1 + m) % 7 != 0:
        print("{:3d}".format(day),end="")
    else:
        print()
        print("{:3d}".format(day),end="")
    day += 1