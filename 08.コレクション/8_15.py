x = {
    "野菜　　": "季節",
    "キャベツ": "春",
    "スイカ　": "夏",
    "ナス　　": "秋",
    "ハクサイ": "冬",
}
for key,value in x.items():
    if value == "季節" or value == "春":
        print(key,":",value,sep="")
    else :
        pass