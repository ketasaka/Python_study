rens = 0
while True:

    #じゃんけんリスト
    j = ["グー","チョキ","パー"]

    #ユーザーの出す手を入力
    print("０：グー　１：チョキ　２：パー")
    i = int(input("じゃんけん！："))

    #プログラム側が出す手をランダムで決定、出力
    import random
    x = random.randrange(3)
    print("ぽん！")
    print(j[x])
    
    print()
    while True:
        if i != 0 and i != 1 and i != 2:
            print("0~2の間から選ばないあなたの負けです")
            rens = 0
            break
        elif x == 1:
            if i == 2:
                print("あなたの負けです")
                rens = 0
                break
            elif i == 0:
                print("あなたの勝ちです")
                rens = rens + 1
                break
            else:
                pass
        elif x == 0:
            if i == 2:
                print("あなたの勝ちです")
                rens = rens + 1
                break
            elif i == 1:
                print("あなたの負けです")
                rens = 0
                break
            else:
                pass
        elif x == 2:
            if i == 1:
                print("あなたの勝ちです")
                rens = rens + 1
                break
            elif i == 0:
                print("あなたの負けです")
                rens = 0
                break
            else:
                pass
        else :
            pass

        print()
        print("０：グー　１：チョキ　２：パー")
        i = int(input("あいこで！："))
        import random

        x = random.randrange(3)
        print("しょ！")
        print(j[x])
    print("ただいま",rens,"連勝中")
    print()

    print("続けますか？ :")
    o = int(input("0:続ける　1:終わる"))
    if o == 1:
        print("プログラムを終了します。")
        break
    elif o == 0:
        print("プログラムを続行します。")
        pass
    else:
        print("既定の数値を入力されなかったため、プログラムを終了します。")
        break