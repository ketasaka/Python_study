n = int(input("入力値："))
for i in range(2,n):
    if n % i == 0:
        print(n,"は素数です。")
        break
    else:
        pass
else:
    print(n,"は素数ではありません。")