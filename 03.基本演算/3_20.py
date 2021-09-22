
hamburger = 450
shake = 200
cola = 100
sum = hamburger + shake + cola
tax = int(sum * 0.1)
chip = int(sum * 0.16)
total = sum + tax + chip
print("ハンバーガー\t：", hamburger)
print("シェイク\t：", shake)
print("コーラ\t\t：", cola)
print("合計額（税抜）\t：", sum)
print("消費税\t\t：", tax)
print("チップ\t\t：", chip)
print("合計額（税込）\t：", sum + tax + chip)