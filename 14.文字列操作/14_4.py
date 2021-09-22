print("文字列を２つ入力してください。")
m = input("１つ目の文字列を入力：")
n = input("２つ目の文字列を入力：")
ml = len(m)
nl = len(n)
if ml == nl :
    for i in range(ml):
        if m[i] == n[i]:
            pass
        else:
            print("違う文字列です。")
            break
    else:
        print("同じ文字列です。")
else:
    print("違う文字列です。")