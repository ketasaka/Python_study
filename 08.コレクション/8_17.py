a = {
    "国語": "75,",
    "算数": "80",
}
b = {
    "国語": "75,",
    "数学": "80",
}
c = {
    "国語": "75,",
    "数学": "80,",
    "理科": "65,",
    "社会": "90,",
    "英語": "70",
}
print("[",end="")
for key,value in a.items():
    print(key,":",value,end="")
print("]")
print("[",end="")
for key,value in b.items():
    print(key,":",value,end="")
print("]")
print("[",end="")
for key,value in c.items():
    print(key,":",value,end="")
print("]")