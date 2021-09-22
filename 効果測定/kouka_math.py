x = ["+","-","×","÷"]

while True:
    print("1.足し算　2.引き算　3.掛け算　4.割り算")
    i = int(input("どんな計算をしますか？"))
    if i == 1 or i == 2 or i == 3 or i == 4:
        break
    else:
        print("正しい値を入力してください。")
        print()

num1 = int(input("１つ目の数字を入力してください："))
num2 = int(input("２つ目の数字を入力してください："))

if i == 1:
    l = num1 + num2 
elif i == 2:
    l = num1 - num2
elif i == 3:
    l = num1 * num2
elif i == 4:
    l = num1 / num2

print("{}　{}　{}　＝ {}".format(num1,x[i - 1],num2,l))