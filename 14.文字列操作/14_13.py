print("住所を入力してください：")
m = input()
if m.count("東京都")==1 or m.count("大阪府")==1 or m.count("京都府")==1 or m.count("北海道")==1:
    c = 3
else:
    c = m.index("県")+1

if m.count("市")==1:
    d = m.index("市")+1
elif m.count("郡")==1:
    d = m.index("郡")+1
else:
    d = m.index("区")+1
print(m[c:d])