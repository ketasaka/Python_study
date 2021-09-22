print("１つ目の住所を入力してください：")
m = input()
print("２つ目の住所を入力してください：")
n = input()

if m.count("市")==1:
    d = m.index("市")+1
    e = n.index("市")+1
    if d == e:
        print("同じ市ですね。ご近所さん。")
    else:
        print("同じ市ではないようです。")
elif m.count("郡")==1:
    d = m.index("郡")+1
    e = n.index("郡")+1
    if d == e:
        print("同じ郡ですね。ご近所さん。")
    else:
        print("同じ郡ではないようです。")
else:
    d = m.index("区")+1
    e = n.index("区")+1
    if d == e:
        print("同じ区ですね。ご近所さん。")
    else:
        print("同じ区ではないようです。")