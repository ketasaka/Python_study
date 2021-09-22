start = int(input("開始数："))
end = int(input("終了数："))
sum = 0
for i in range(start,end+1):
    sum = sum + i
print("合計：",sum)