#味方 [名前,HP,攻撃,素早さ]
yusya = ["勇者",50,15,30]
suraimu = ["スライム",60,3,15]
doraki = ["ドラキー",30,10,45]

#敵
import random

teki_hp = random.randint(100,200)
teki_kougeki = random.randint(10,30)


teki = ["敵",250,10,29]

#攻撃フェーズ
import time
kyara = [yusya,suraimu,doraki,teki]
mikata = [yusya,suraimu,doraki]

for l in range(3,0,-1):
    for i in range(0,l,1):
        if kyara[i][3] < kyara[i + 1][3]:
            kyara[i],kyara[i + 1] = kyara[i + 1],kyara[i]
        else:
            pass
#kyara = [doraki,yusya,teki,suraimu] になる

teki_kougeki = 2

while True:
    for i in range(4):
        if kyara[i][1] <= 0:
            pass
        else:
            print(kyara[i][0],"の攻撃")
            time.sleep(0.5)
            if kyara[i] != teki:
                print("敵に{}のダメージ".format(kyara[i][2]))
                teki[1] -= kyara[i][2]
                if teki[1] <= 0:
                    print()
                    break
                else:
                    print("敵の残りHP：{}".format(teki[1]))
                    pass
            else:
                import random
                tage = random.randint(0,teki_kougeki)
                print("{}に{}のダメージ".format(mikata[tage][0],teki[2]))
                mikata[tage][1] -= teki[2]
                if mikata[tage][1] <= 0:
                    print("{}が倒れました。".format(mikata[tage][0]))
                    del mikata[tage]
                    teki_kougeki -= 1
                else:
                    print("{}の残りHP：{}".format(mikata[tage][0],mikata[tage][1]))
            print()
            time.sleep(1)
    
    if teki[1] <= 0:
        print("敵が倒れました。")
        print("あなたの勝ちです。")
        break
    else:
        pass

    if teki_kougeki == -1:
        print("味方が全滅しました。")
        print("あなたの負けです。")
        break
    else:
        pass