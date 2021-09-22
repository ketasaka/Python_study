def kansu(ans = "?"):
    listA = list(range(2,500,3))
    if ans in listA:
        return "seikai"
    elif ans == "?":
        return
    else:
        return "hu"

