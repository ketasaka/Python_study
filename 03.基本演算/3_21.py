import random
a = random.randint(0,9)
b = random.randint(0,9)
c = random.randint(0,9)
d = random.randint(0,9)
sum = (a+b*c-d)
print(a,"+",b,"×",c,"-",d,"=")
print("計算結果は？:",end="")
e = input()
n = int(e)
if n == sum:
    print("正解です！")
else:
    print("不正解です。正解は",sum,"です。",sep="")