a = {}
sum = 0
for i in range(3):
    l = input("{}人目の名前を入力してください".format(i + 1))
    m = int(input("{}人目の点数を入力してください".format(i + 1)))
    a[l] = m

for key,value in a.items():
    if value >= 60:
        print(key,"さんは合格です。",sep="")
    else:
        print(key,"さんは不合格です。",sep="")
    sum += value

sum = int(sum / 3 * 100)
sum = sum / 100

print("平均点は、{}点です。".format(sum))