print("0～100 までの値（整数値）を３つ入力してください")
l = int(input("１つ目の値："))
m = int(input("２つ目の値："))
n = int(input("３つ目の値："))

if l == m ==n:
    print("同じ値です")
else:
    l,m,n = sorted([l,m,n])
    print("値が大きいのは",n,"です")