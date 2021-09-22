print("0～100 までの得点（整数値）を２つ入力してください")
n = int(input("国語の得点："))
m = int(input("英語の得点："))

if n == 100:
    if m == 100:
        print("満点です")