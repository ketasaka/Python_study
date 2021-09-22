a = [4,10,59,679,1991,3994,6789,19324]
add = 0
def sum(ans,a):
    ans = ans + a
    return ans

for i in range(8):
    add = sum(add,a[i])

print("合計値 = ",add)