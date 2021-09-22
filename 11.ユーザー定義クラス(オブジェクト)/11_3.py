class enzan:
    
    def __init__(self, start: int, end: int):

        self.start = start
        self.end = end

    def keisan(self):
        sum = 0
        for i in range(self.start,self.end+1):
            sum += i
        return sum

    def enzan(self):
        print("{}から{}までの合計値は{}です。".format(self.start,self.end,self.keisan()))


x = 100
y = 200

goukei = enzan(x,y)

goukei.enzan()