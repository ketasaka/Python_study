color = {
    "赤":"red",
    "白":"white",
    "黒":"black",
    "青":"blue",
    "緑":"green",
}
def rensou(color):
    for key,value in color.items():
        print(key,":",value,sep="")

rensou(color)