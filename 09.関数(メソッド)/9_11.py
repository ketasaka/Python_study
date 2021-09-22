def unnsei():
    import random
    x = random.randint(0,3)
    return x

a = ["絶好調","好調","不調","絶不調"]

i = unnsei()

print("今日の運勢：{}".format(a[i]))