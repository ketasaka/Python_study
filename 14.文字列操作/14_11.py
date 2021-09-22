print("住所を入力してください：")
m = input()
if m.count("市") > 0:
    print("市")
elif m.count("郡") > 0:
    print("郡")
else:
    print("東京２３区")