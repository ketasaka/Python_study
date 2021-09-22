def renraku():
    komasu = 3
    jugyo(komasu)
    return komasu

def jugyo(komasu):
    kamoku = ["HR","Python実習"]
    for i in range(komasu + 1):
        if i == 0:
            print("HR")
        else:
            if i >= len(kamoku):
                print(i,"コマ目:",kamoku[len(kamoku) - 1],sep="")
            else:
                print(i,"コマ目:",kamoku[i],sep="")
komasu = renraku()
print("共通問題集：１０定義済みクラス（オブジェクト）＆１１ユーザー定義クラス（オブジェクト）¥n コマ数：",komasu)