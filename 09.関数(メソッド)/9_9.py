def around(r):
    ans = 2 * r * 3.14
    return ans

def heiho(r):
    import math
    x = math.pi
    ans = r * r * x
    return ans

r = float(input("半径を入力してください。"))

around = int(around(r) * 100) / 100
heiho = int(heiho(r) * 100) / 100

print("半径{}の円周は{}".format(r,around))
print("半径{}の面積は{}".format(r,heiho))