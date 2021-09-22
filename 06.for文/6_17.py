for i in range(1,53):
    for j in range(0,7):
        if j == 0:
            print(i,"週目")
        elif j == 1:
            print(i,"週目 月曜日・・・1時間")
        elif j == 2:
            print(i,"週目 火曜日・・・2時間")
        elif j == 3:
            print(i,"週目 水曜日・・・3時間")
        elif j == 4:
            print(i,"週目 木曜日・・・4時間")
        elif j == 5:
            print(i,"週目 金曜日・・・5時間")
        elif j == 6 and i % 2 == 1:
            print(i,"週目 土曜日・・・6時間")
            print(i,"週目 日曜日・・・お休み")
        else:
            print(i,"週目 土曜日・・・お休み")
            print(i,"週目 日曜日・・・7時間")
    print()
sum = 26 * 43
print("合計:",sum,"時間")