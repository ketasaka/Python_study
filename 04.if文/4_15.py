print("0～100 までの値（整数値）を２つ入力してください")
n = int(input("１つ目の値："))
m = int(input("２つ目の値："))

if n == m :
    print("同じ値です")
else:
    n,m = sorted([n,m])
    print("値が大きいのは",m,"です")