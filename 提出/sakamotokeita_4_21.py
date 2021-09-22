l = int(input("国語の得点"))
m = int(input("数学の得点"))
n = int(input("英語の得点"))

if l + m + n >= 230:
    print("合格")
elif l + m + n >= 210 and (l >= 85 or m >= 85 or n >=85):
    print("合格")
else:
    print("補講対象")