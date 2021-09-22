n = int(input("0～100 までの得点（整数値）を入力してください"))

if n < 0 or n > 100:
    print("入力値が不正です")
if n == 100:
    print("満点合格です")
elif n >= 60:
    print("合格です")
else :
    print("不合格です")