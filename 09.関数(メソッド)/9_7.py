a = [4,10,59,679,1991,3994,6789,19324]
c = 0
def sum(x,y):
    if x == y:
        c = 1
        return c
    else:
        pass
        
b = int(input("整数を入力してください："))
for i in range(8):

    c = sum(b,a[i])
    if c == 1:
        print(b,"は配列に含まれています。")
        break
    else:
        pass
else:
    print(b,"は配列に含まれていません。")