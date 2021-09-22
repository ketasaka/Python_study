print("長方形を描画します")
print("2~20までの整数を入力してください")
for _ in range(2):
    n = int(input("行数の入力:"))
    m = int(input("列数の入力:"))
    if n >= 2 and n <= 20 and m >= 2 and m <=20:
        break
    else:
        print("値が正しくありません。")
for i in range(1,n+1):
    for j in range(1,m+1):
        print("*",end="")
    print()