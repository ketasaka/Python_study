print("直角三角形を描画します")
print("2~20までの整数を入力してください")
n = int(input("底辺の長さを入力:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print()