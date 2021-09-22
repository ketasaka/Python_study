h = float(input("身長(cm)を入力してください："))
w = float(input("体重(kg)を入力してください："))

def BMI():
    bmi = int(w / h / h * 1000000)
    bmi = bmi / 100
    return bmi

def tekisei():
    teki = int(h * h / 100 * 22)
    teki = teki / 100
    return teki

bmi = BMI()
teki = tekisei()

print("BMI値は{}です".format(bmi))
print("適性体重は{}です".format(teki))