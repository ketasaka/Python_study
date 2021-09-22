f = open("16_4_write.txt","w")
while True:
    mozi = input("入力：")
    if mozi == "end":
        break
    f.write("{}\n".format(mozi))
f.close()
