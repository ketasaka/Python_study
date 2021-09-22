import random

class Coin:
    
    x = [1,5,10,50,100,500]
    y = [0,0,0,0,0,0]

    #ランダム生成
    def addCOINS(self):
        a = random.randint(0,5)
        return a

    #コインの枚数の追加
    def getCOUNT(self):
        for _ in range(10):
            i = self.addCOINS()
            Coin.y[i] += 1

        for l in range(6):
            print("{}円:{}枚 ".format(Coin.x[l],Coin.y[l]),end="")

        print()
        self.getAMOUNT()

    #金額の集計
    def getAMOUNT(self):
        sum = 0

        for i in range(6):
            sum = Coin.x[i] * Coin.y[i] + sum

        print("総額：{}円".format(sum))


coin = Coin()
coin.getCOUNT()