x = {
    "id": "100",
    "name": "大原太郎",
    "age": "19",
}
y = {
    "id": "100",
    "name": "大原太郎",
    "age": "20",
}
x.update(y)
for key,value in x.items():
    print(key,":",value,sep="")