print("１からｎまでの和を求めます")

while True:
    n = int(input("ｎの値"))
    if n > 0:
        break

sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("1から",n,"までの和は",sum,"です。")