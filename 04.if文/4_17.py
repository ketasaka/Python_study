print("0～100 までの値（整数値）を２つ入力してください")
n = int(input("１つ目の値："))
m = int(input("２つ目の値："))

if n == m :
    print(n)
else:
    n,m = sorted([n,m])
    print(m)
    print(n)