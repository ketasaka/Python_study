n = int(input("西暦を入力してください"))
if n % 400 == 0:
    print("閏年です")
elif n % 100 == 0:
    print("平年です")
elif n % 4 == 0:
    print("閏年です")
else:
    print("平年です")