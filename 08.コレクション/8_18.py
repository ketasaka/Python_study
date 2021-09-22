ave = 0
x = {
    "商品A": "500",
    "商品B": "2030",
    "商品C": "1980",
}
for value in x.values():
    ave = ave + value
ave = ave / 3
y = {
    "商品A": "500",
    "商品B": "2030",
    "商品C": "1980",
    "平均": ave,
}
x.update(y)
print("<現在の在庫>")
print(x)