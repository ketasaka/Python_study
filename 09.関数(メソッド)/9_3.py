def hyouzi(x,n):
    for _ in range(n):
        print(x)

while True:
    x = input("文字列：")
    n = int(input("回数："))
    hyouzi(x,n)