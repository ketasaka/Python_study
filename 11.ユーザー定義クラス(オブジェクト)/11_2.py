class enzan:
    def enzan(a,b):
        sum = 0
        for i in range(a,b+1):
            sum += i
        return sum


x = 100
y = 200
a = enzan.enzan(x,y)
print("{}から{}までの合計値は{}です。".format(x,y,a))