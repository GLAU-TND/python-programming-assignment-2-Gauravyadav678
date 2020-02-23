a=[10, 7, 76, 415]
b=[]
for i in a:
    if i<=9:
        b.insert(0,i)
    elif i>=11 and i<=100:
        b.insert(1,i)
    elif i>=100 and i<=999:
        b.insert(2,i)
    elif i>=10 and i<=11:
        b.insert(3,i)
for i in b:
    print(i, end="")
